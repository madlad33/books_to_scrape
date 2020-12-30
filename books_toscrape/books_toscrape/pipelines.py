# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class BooksToscrapePipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta={'bookname': item.get('book_name')}) for u in urls]

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'full/{request.meta["bookname"]}.jpg'
