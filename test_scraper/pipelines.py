import psycopg2
from itemadapter import ItemAdapter # noqa


class TestScraperPipeline(object):
    def open_spider(self, spider):
        hostname = '127.0.0.1'
        username = 'parsing_admin'
        password = 'parsing_adminparsing_admin'
        database = 'parsing'
        port = "5444"
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()
        self.create_tables()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def create_tables(self):
        """create tables in the database if they are not contained"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Table_1
             (
             id TEXT PRIMARY KEY,
             url TEXT NOT NULL,
             site_title TEXT,
             meta_description TEXT,
             html_lang TEXT,
             score INT2,
             department TEXT
             );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Table_2
             (
             id SERIAL PRIMARY KEY,
             url_id TEXT,
             a_href TEXT,
             a TEXT,
             alt TEXT,
             h1 TEXT,
             h2 TEXT,
             h3 TEXT,
             h4 TEXT,
             h5 TEXT,
             p TEXT,
             FOREIGN KEY (url_id) REFERENCES Table_1 (id) ON DELETE CASCADE
             );''')

        self.connection.commit()

    def process_item(self, item, spider):
        self.cur.execute(
            """INSERT INTO Table_1 (id, url, site_title, Meta_description, html_lang, score, department)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""", (
                item['uuid'],
                item['url'],
                item['site_title'],
                item['meta_description'],
                item['html_lang'],
                item['score'],
                item['department']
                )
        )

        self.cur.execute(
            """INSERT INTO Table_2 (url_id, a_href, a, alt, h1, h2, h3, h4, h5, p)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
                item['uuid'],
                item['a_href'],
                item['a'],
                item['alt'],
                item['h1'],
                item['h2'],
                item['h3'],
                item['h4'],
                item['h5'],
                item['p'],
                )
        )
        self.connection.commit()
        return item
