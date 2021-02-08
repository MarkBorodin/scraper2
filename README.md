# INSTALL_APP


### Setup

clone repository:
```
git clone https://github.com/MarkBorodin/scraper2.git
```
move to folder "scraper2":
```
cd scraper2
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

to create tables run file:
```
create_db.py
```

run spider with url. Enter url via command line:
```
scrapy crawl spider_name -a home_page='your_url'
```

For example:

```
scrapy crawl sitemap_spider -a home_page='https://www.sos-kinderdorf.ch/'
```

### Finish
