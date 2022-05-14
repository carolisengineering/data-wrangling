import os
import psycopg


DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = 'data_wrangling' 


def main():
        conn = psycopg.connect(
                host="localhost",
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD
        )
        cur = conn.cursor()

        cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                        'email varchar (100) NOT NULL,'
                        'name varchar (1000) NOT NULL,'
                        'password varchar(100) NOT NULL,'
                        'created_at timestamp DEFAULT CURRENT_TIMESTAMP);'
        )

        conn.commit()
        cur.close()
        conn.close()

if __name__=="__main__":
        main()