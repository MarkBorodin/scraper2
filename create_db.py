import psycopg2


class DB(object):
    def open(self):
        hostname = '127.0.0.1'
        username = 'parsing_admin'
        password = 'parsing_adminparsing_admin'
        database = 'parsing'
        port = "5444"
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()

    def close(self):
        self.cur.close()
        self.connection.close()

    def drop_table(self):
        self.cur.execute(
            """DROP TABLE table_1"""
        )
        self.connection.commit()

    def create_tables(self):
        """create tables in the database if they are not contained"""

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Home_Page
                     (
                     id TEXT PRIMARY KEY,
                     url TEXT,
                     sitemap_exists boolean
                     );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Subpage
                     (
                     id TEXT PRIMARY KEY,
                     url TEXT,
                     indexed_in_sitemap boolean,
                     robots_follow_no_follow boolean,
                     home_page TEXT,
                     FOREIGN KEY (home_page) REFERENCES Home_Page (id) ON DELETE CASCADE
                     );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS H1
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS H2
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS H3
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS H4
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS H5
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS P
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS A
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS title
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS meta
                    (
                    id SERIAL PRIMARY KEY,
                    text TEXT,
                    appearance_position INT,
                    subpage TEXT,
                    FOREIGN KEY (subpage) REFERENCES Subpage (id) ON DELETE CASCADE
                    );''')

        self.connection.commit()


db = DB()
db.open()
db.create_tables()
db.close()
