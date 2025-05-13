# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy import Request
from itemadapter import ItemAdapter
import re


class MyanimelistPipeline:
    def process_item(self, item, spider):
        return item


class CustomImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # Generate requests for the image URLs
        if "image_urls" in item:
            for image_type, image_url in item["image_urls"].items():
                if image_type == "characters":
                    # Handle character images
                    for charater_name, charater_link in image_url.items():
                        if charater_name and charater_link["character"]:
                            yield Request(charater_link["character"], meta={"anime_id": item["id"], "image_type": image_type, "character_name": charater_name, "character_type": "character"})
                        if charater_name and charater_link["voice_actor"]:
                            yield Request(charater_link["voice_actor"], meta={"anime_id": item["id"], "image_type": image_type, "character_name": charater_name, "character_type": "voice_actor"})
                else:

                    yield Request(image_url, meta={"anime_id": item["id"], "image_type": image_type})

    def file_path(self, request, response=None, info=None, *, item=None):
        # Use the anime ID and image type as the filename
        anime_id = request.meta.get("anime_id", "unknown")
        image_type = request.meta.get("image_type", "unknown")
        url_without_query = request.url.split('?')[0]
        image_extension = os.path.splitext(url_without_query)[1]

        if image_type == "characters":
            self.character_name = request.meta.get("character_name", "unknown")
            character_type = request.meta.get("character_type", "unknown")

            # Ensure character_name is sanitized
            sanitized_name = re.sub(
                r'[^\w\-_]', '_', self.character_name) if self.character_name else "unknown_character"

            if character_type == "character":
                # For character images
                return f"{image_type}_{anime_id}_{sanitized_name}{image_extension}"
            elif character_type == "voice_actor":
                # For voice actor images
                return f"{image_type}_{anime_id}_{sanitized_name}_voiceActor{image_extension}"
            else:
                # Handle unexpected character types
                return f"{image_type}_{anime_id}_{sanitized_name}_unknown{image_extension}"

        # Default filename for other image types
        return f"{image_type}_{anime_id}{image_extension}"
