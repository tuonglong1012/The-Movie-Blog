import scrapy
from scrapy.crawler import CrawlerProcess
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Movie,MovieDetail,Character,MovieReview
import json
import os

router = APIRouter()


def get_movie():
    process = CrawlerProcess(settings={
        "BOT_NAME": "myanimelist",
        "ROBOTSTXT_OBEY": True,
        "FEEDS": {
            "data/data.json": {
                "format": "json",
                "overwrite": True,
            },
        },
    })
    process.crawl(TopanimeCraw1lSpider)
    process.start()  # the script will block here until the crawling is finished
    return "Crawling completed"
class TopanimeCraw1lSpider(scrapy.Spider):
    name = "topanime_craw1l"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        # Extract the anime titles and their corresponding URLs
        urls = response.css(
            ".anime_ranking_h3 a::attr(href)").getall()

        for url in urls:
            yield response.follow(url, self.parse_anime)
        # yield response.follow(urls[0], self.parse_anime)

    def parse_anime(self, response):
        # Extract the title, score, and rank

        title = response.css("h1.title-name strong::text").get()

        score = response.css(".score-label::text").get()

        rank = response.css(".ranked strong::text").get().replace("#", "")

        episodes = response.css(
            "div.spaceit_pad:nth-child(18)::text").re_first(r'\d+')
        if not episodes:
            episodes = response.css(
                "div.spaceit_pad:nth-child(17)::text").re_first(r'\d+')

        status = response.css(
            "div.spaceit_pad:nth-child(19)::text").getall()

        Synopsis = response.css(
            "p[itemprop=description]::text").getall()

        link = response.url

        id = link.split('/')[4]

        test = {}
        for i, section in enumerate(response.css(".spaceit_pad")):
            if section and i != 2:
                tilte = section.css(".dark_text::text").get()
                test[tilte] = " ".join(
                    [line.strip().replace("\"", "") for line in section.css("::text").getall() if line.strip()])

        characters = response.css("td.pb24 table")

        test["characters"] = {}
        for character in characters:
            test["characters"][character.css(".h3_characters_voice_actors a::text").get()] = {
                "role": character.css(
                    ".h3_characters_voice_actors + .spaceit_pad small::text").get(),
                "link": character.css(
                    ".h3_characters_voice_actors a::attr(href)").get(),
                "voice_actor": character.css(
                    "td.pr4 a::text").get(),
                "voice_actor_link": character.css(
                    "td.pr4 a::attr(href)").get(),
                "voice_actor_country": character.css(
                    "td.pr4 small::text").get(),
            }

        reviews = response.css(".review-element")

        test["reviews"] = {}
        for review in reviews:
            test["reviews"][review.css(".username a::text").get()] = {
                "show": review.css(".text::text").getall(),
                "hidden": review.css(".text .js-hidden::text").getall(),
            }

        return {
            "title": title,
            "id": id,
            "score": score,
            "rank": rank,
            "status": status,
            "episodes": episodes,
            "synopsis": Synopsis,
            "link": link,
            "test": test,
            # "producer": producer,
        }


@router.post("/import-json")
def import_movies(db: Session = Depends(get_db)):
    json_path = os.path.join("data", "data.json")

    try:
        with open(json_path, "r", encoding="UTF-8") as f:
            movies_data = json.load(f)

        if not isinstance(movies_data, list):
            raise HTTPException(status_code=400, detail="File JSON phải là danh sách các đối tượng.")

        for movie in movies_data:
            title = movie.get("title", "Unknown Title")
            if not title:
                raise HTTPException(status_code=400, detail="Title is required for the movie.")
            # Thêm phim vào bảng movies
            movie_test = movie.get("test", {})
            newMovie = Movie(
                external_id=movie.get("id"),
                title=title,
                rank=movie.get("rank"),
                episodes=movie.get("episodes"),
                score=movie.get("score"),
                type=movie_test.get("Type:", "").replace("Type:", "").strip(),
                aired=movie_test.get("Aired:", "").replace("Aired:", "").strip(),
                members=movie_test.get("Members:", "").replace("Members:", "").strip()
            )
            db.add(newMovie)
            db.commit()

            synopsis_raw = movie.get("synopsis", "")
            if isinstance(synopsis_raw, list):
                # Lọc bỏ các chuỗi chỉ chứa khoảng trắng hoặc xuống dòng, đồng thời làm sạch ký tự xuống dòng
                cleaned = [line.strip() for line in synopsis_raw if line.strip()]
                # Kết nối các phần tử lại với nhau bằng dấu cách
                synopsis_text = " ".join(cleaned)
            elif isinstance(synopsis_raw, str):
                synopsis_text = synopsis_raw.strip()
            else:
                synopsis_text = ""
            # Đảm bảo loại bỏ hoàn toàn các ký tự xuống dòng trong cuối cùng
            synopsis_text = synopsis_text.replace("\r\n", " ").replace("\n", " ")



            movie_id = newMovie.id     
            newMovieDetail = MovieDetail(
                movie_id=movie_id,
                score=movie.get("score"),
                title=title,
                rank=movie.get("rank"),
                status=movie.get("status"),
                episodes=movie.get("episodes"),
                synopsis=synopsis_raw,
                link=movie.get("link"),
                synonyms=movie_test.get("Synonyms:", "").replace("Synonyms:", "").strip(),
                japanese=movie_test.get("Japanese:", "").replace("Japanese:", "").strip(),
                type=movie_test.get("Type:", "").replace("Type:", "").strip(),
                aired=movie_test.get("Aired:", "").replace("Aired:", "").strip(),
                premiered=movie_test.get("Premiered:", "").replace("Premiered:", "").strip(),  
                broadcast=movie_test.get("Broadcast:", "").replace("Broadcast:", "").strip(),
                producers=movie_test.get("Producers:", "").replace("Producers:", "").strip(),
                licensors=movie_test.get("Licensors:", "").replace("Licensors:", "").strip(),
                studios=movie_test.get("Studios:", "").replace("Studios:", "").strip(),
                source=movie_test.get("Source:", "").replace("Source:", "").strip(),
                genres=movie_test.get("Genres:", "").replace("Genres:", "").strip(),
                demographic=movie_test.get("Demographic:", "").replace("Demographic:", "").strip(),
                duration=movie_test.get("Duration:", "").replace("Duration:", "").strip(),
                rating=movie_test.get("Rating:", "").replace("Rating:", "").strip(),
                popularity=movie_test.get("Popularity:", "").replace("Popularity:", "").strip(),
                members=movie_test.get("Members:", "").replace("Members:", "").strip(),
                favorites=movie_test.get("Favorites:", "").replace("Favorites:", "").strip(),
            )
            db.add(newMovieDetail)
            db.commit()

            movie_detail_id = newMovieDetail.id

            # Thêm các nhân vật
            characters_data = movie_test.get("characters", {})
            for name, character_data in characters_data.items():
                if name == "null":
                    continue
                newCharacter = Character(
                    movie_detail_id=movie_detail_id,
                    name=name,
                    role=character_data.get("role"),
                    link=character_data.get("link"),
                    voice_actor=character_data.get("voice_actor"),
                    voice_actor_link=character_data.get("voice_actor_link"),
                    voice_actor_country=character_data.get("voice_actor_country")
                )
                db.add(newCharacter)

            # Thêm các review
            reviews_data = movie_test.get("reviews", {})
            for username, review_data in reviews_data.items():
                newReview = MovieReview(
                    movie_detail_id=movie_detail_id,
                    username=username,
                    show_reviews=",".join(review_data.get("show", [])),
                    hidden_reviews=",".join(review_data.get("hidden", []))
                )
                db.add(newReview)

            # Commit toàn bộ nhân vật và review
            db.commit()

        return {"message": f"Đã thêm {len(movies_data)} phim vào cơ sở dữ liệu."}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Không tìm thấy file JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




def get_all_movies(db: Session): 
    return db.query(Movie).all()