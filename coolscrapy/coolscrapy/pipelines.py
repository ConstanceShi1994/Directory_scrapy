# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime 
import redis
import json
import logging
from contextlib import contextmanager 

from scrapy import signals
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from coolscrapy.models import News, db_connect, create_news_table, Article

class CoolscrapyPipeline(object):
	def __init__(self):

	def open_spider(self, spider):

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
