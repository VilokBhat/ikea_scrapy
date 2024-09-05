# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class IkeaScrapyPipeline:
    def open_spider(self, spider):
            self.conn = sqlite3.connect('ikea_prod.db')
            self.c = self.conn.cursor()
            self.c.execute("""DROP TABLE IF EXISTS products""")
            self.c.execute('''
                           CREATE TABLE IF NOT EXISTS products (
                               name TEXT,
                               descri TEXT,
                               price TEXT
                        )
                ''')
            #self.conn.close()
            
#    def close_spider(self, spider):
#         if hasattr(self, 'conn'):
#            self.conn.commit()
#            self.conn.close()
        
    def process_item(self, item, spider):
        if hasattr(self, 'conn'):
            self.c.execute('''
                INSERT INTO products (name, descri, price) VALUES (?, ?, ?)
            ''', (item.get('name'), item.get('descri'), item.get('price')))
            self.conn.commit()
        return item