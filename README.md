# INSTALL_APP


### Setup

clone repository:
```
git clone https://github.com/MarkBorodin/scraper.git
```
move to folder "scraper":
```
cd scraper
```

### run database

run on command line in the project folder:

```
docker-compose up -d
```

you need to create database. Run on command line:
```
docker-compose exec postgresql bash
```
next step:
```
su - postgres
```
next step:
```
psql
```
next step (you can create your own user, change password and other data):
```
CREATE DATABASE parsing; 
CREATE USER parsing_admin WITH PASSWORD 'parsing_adminparsing_admin';
ALTER ROLE parsing_admin SET client_encoding TO 'utf8';
ALTER ROLE parsing_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE parsing_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE parsing TO parsing_admin;
ALTER USER parsing_admin CREATEDB;

```
to install the required libraries, run on command line:
```
pip install -r requirements.txt
```

### the first way to parse data - using pyppeteer, bs4:

to parse the data and write it to the database (and create tables in the database if not contained), run:
```
test_task_parser.py
```


### second way to parse data - using Scrapy, scrapy-splash, bs4:

move to folder "test_scraper":
```
cd test_scraper
```

pull the image for scrapy-splash:

```
sudo docker pull scrapinghub/splash
```

start the container:
```
sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```

run spider:
```
scrapy crawl myspider
```

###all data will be written to the database
### Finish
