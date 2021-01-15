import asyncio
import random
import uuid

import psycopg2
from bs4 import BeautifulSoup
from pyppeteer import launch


# insert url here and run the code
url = 'https://www.sos-kinderdorf.ch/'


async def get_html(url):
    """get html after javascript execution on the page"""
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url, waitUntil='networkidle2')
    content = await page.content()
    await browser.close()
    return content


def get_page_data(html):
    """parsing the required data"""
    soup = BeautifulSoup(html, 'lxml')
    site_title = soup.title.string
    meta_description = soup.find('head').find_all('meta')
    html_lang = soup.find('html').get('lang')
    a_href = [href.get('href') for href in soup.find_all('a')]
    a = soup.find_all('a')
    alt = [alt.get('alt') for alt in soup.find_all('img')]
    h1 = [h1.text.strip() for h1 in soup.find_all('h1')]
    h2 = [h2.text.strip() for h2 in soup.find_all('h2')]
    h3 = [h3.text.strip() for h3 in soup.find_all('h3')]
    h4 = [h4.text.strip() for h4 in soup.find_all('h4')]
    h5 = [h5.text.strip() for h5 in soup.find_all('h5')]
    p = [p.text.strip() for p in soup.find_all('p')]
    data = {
        'uuid': str(uuid.uuid1()),
        'url': str(url),
        'site_title': str(site_title),
        'meta_description': str(meta_description),
        'html_lang': str(html_lang),
        'a_href': str(a_href),
        'a': str(a),
        'alt': str(alt),
        'h1': str(h1),
        'h2': str(h2),
        'h3': str(h3),
        'h4': str(h4),
        'h5': str(h5),
        'p': str(p),
        'score': random.randint(1, 101),
        'department': random.choice(['Government', 'School', 'Non-Profit', 'Marketing', 'Development']),
    }
    return data


def connect_to_db():
    """connect to database"""
    con = psycopg2.connect(
        database="parsing",
        user="parsing_admin",
        password="parsing_adminparsing_admin",
        host="127.0.0.1",
        port="5444"
    )
    print("Database opened successfully")
    return con


def create_tables(con):
    """create tables in the database if they are not contained"""
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Table_1
         (
         id TEXT PRIMARY KEY,
         url TEXT NOT NULL,
         site_title TEXT,
         meta_description TEXT,
         html_lang TEXT,
         score INT2,
         department TEXT
         );''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Table_2
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

    con.commit()


def write_to_db(data, con):
    """writing data to the database"""
    cur = con.cursor()

    cur.execute(
        """INSERT INTO Table_1 (id, url, site_title, meta_description, html_lang, score, department)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""", (
            data['uuid'],
            data['url'],
            data['site_title'],
            data['meta_description'],
            data['html_lang'],
            data['score'],
            data['department']
        )
    )

    cur.execute(
        """INSERT INTO Table_2 (url_id, a_href, a, alt, h1, h2, h3, h4, h5, p)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
            data['uuid'],
            data['a_href'],
            data['a'],
            data['alt'],
            data['h1'],
            data['h2'],
            data['h3'],
            data['h4'],
            data['h5'],
            data['p'],
        )
    )
    con.commit()
    print("Records inserted successfully")
    con.close()


def main():
    # parse data using pyppeteer library
    html = asyncio.get_event_loop().run_until_complete(get_html(url))
    # get the data and write it to the dictionary
    data = get_page_data(html)
    # connect to the database
    con = connect_to_db()
    # ..and create tables if not contained
    create_tables(con)
    # writing data
    write_to_db(data, con)


if __name__ == '__main__':
    main()
