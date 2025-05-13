from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import scrapy
from myanimelist.items import MyanimelistItem
import re


class TopanimeCraw1lSpider(scrapy.Spider):
    name = "topanime_craw1l"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]
    count = 0  # Initialize count as a class attribute

    def __init__(self, myarg=None, **kwargs):
        super().__init__(**kwargs)
        self.myarg = myarg

    def parse(self, response):
        if not self.count:
            self.count = 0

        self.count += 1

        # Extract the anime titles and their corresponding URLs
        urls = response.css(".word-break")
        for url in urls:
            print(self.myarg)
            small_cover = url.css("img::attr(data-src)").get()
            yield response.follow(url.css(
                ".anime_ranking_h3 a::attr(href)").get(), self.parse_anime, meta={"small_cover": small_cover})

        # small_cover = urls[0].css("img::attr(data-src)").get()
        # yield response.follow(urls[0].css(
        #     ".anime_ranking_h3 a::attr(href)").get(), self.parse_anime, meta={"small_cover": small_cover})

        # Extract the next page URL and follow it if it exists
        if response.css("a.next") and self.count < 1:
            yield response.follow(
                response.css("a.next::attr(href)").get(), self.parse)

    def parse_anime(self, response):
        # Extract the title, score, and rank

        cover = response.css(".leftside img::attr(data-src)").get()

        image_urls = {}
        image_urls["cover"] = cover
        image_urls["small_cover"] = response.meta["small_cover"]

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
        image_urls["characters"] = {}
        for character in characters:

            character_name = character.css(
                ".h3_characters_voice_actors a::text").get()
            character_link = character.css("img::attr(data-src)").get()

            if character_name and character_link:
                voice_actor = character.css("img::attr(data-src)").getall()
                image_urls["characters"][character_name] = {
                    "character": character_link,
                    "voice_actor": voice_actor[1] if len(voice_actor) > 1 else None
                }

            test["characters"][f"{character_name}"] = {
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
                f"{character_name}_path": f"characters_{id}_{re.sub(
                    r'[^\w\-_]', '_', character_name)}.jpg" if character_name else None,
                f"{character_name}_voice_actor_link": f"characters_{id}_{re.sub(
                    r'[^\w\-_]', '_', character_name)}_voiceActor.jpg" if character_name else None,
            }

        reviews = response.css(".review-element")

        test["reviews"] = {}
        for review in reviews:
            test["reviews"][review.css(".username a::text").get()] = {
                "show": review.css(".text::text").getall(),
                "hidden": review.css(".text .js-hidden::text").getall(),
            }

        item = MyanimelistItem()
        item["covers_path"] = f"cover_{id}.jpg"
        item["small_cover_path"] = f"small_cover_{id}.jpg"
        item["title"] = title
        item["id"] = id
        item["score"] = score
        item["rank"] = rank
        item["status"] = status
        item["episodes"] = episodes
        item["synopsis"] = Synopsis
        item["link"] = link
        item["test"] = test
        item['image_urls'] = image_urls
        yield item

        # if __name__ == "__main__":
        #     from scrapy.settings import Settings

        #     # Define explicit settings
        # settings = Settings()
        # settings.set("BOT_NAME", "myanimelist")
        # settings.set("ROBOTSTXT_OBEY", True)

        # process = CrawlerProcess(settings)
        # process.crawl(TopanimeCraw1lSpider)
        # process.start()
