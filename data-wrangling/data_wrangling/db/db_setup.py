import os
import psycopg2


DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = 'data_wrangling' 


def main():
        conn = psycopg2.connect(
                host="localhost",
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD
        )
        cur = conn.cursor()

        cur.execute('CREATE TABLE users (id varchar(50) PRIMARY KEY,'
                        'email varchar (100) NOT NULL,'
                        'name varchar (100) NOT NULL,'
                        'password varchar(100),'
                        'created_at timestamp DEFAULT CURRENT_TIMESTAMP);'
        )

        conn.commit()
        cur.close()
        conn.close()

if __name__=="__main__":
        main()