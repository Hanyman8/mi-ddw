# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from . import items


class Hw1Pipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        if isinstance(item, items.Article):
            item['type'] = 'article'
            return item
        elif isinstance(item, items.Photogallery):
            item['type'] = 'gallery'
            return item
