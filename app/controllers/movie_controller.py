import scrapy
from scrapy.crawler import CrawlerProcess
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Movie
import json
import os

router = APIRouter()


@router.post("/import-json")
def import_movies(db: Session = Depends(get_db)):
    json_path = os.path.join("data", "test1.json")
    try:
        with open(json_path, "r", encoding="UTF-8") as f:
            movies_data = json.load(f)
        if not isinstance(movies_data, list):
            raise HTTPException(
                status_code=400, detail="File JSON phải là danh sách các đối tượng.")
        for movie in movies_data:
            newMovie = Movie(
                title=movie.get("title"),
                rank=movie.get("rank"),
                episodes=movie.get("episodes"),
                score=movie.get("score"),
                external_id=movie.get("id"),
                type=movie.get("test", {}).get("Type"),
                aired=movie.get("test", {}).get("Aired"),
                members=movie.get("test", {}).get("Members"),
            )
            db.add(newMovie)

        db.commit()
        return {"message": f"Đã thêm {len(movies_data)} phim vào cơ sở dữ liệu."}

    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail="Không tìm thấy file JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_movie():
    process = CrawlerProcess(settings={
        "BOT_NAME": "myanimelist",
        "ROBOTSTXT_OBEY": True,
        "FEEDS": {
            "app/data/data.json": {
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
