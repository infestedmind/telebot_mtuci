import psycopg2

from config import DATABASE, USER, PASSWORD

conn = psycopg2.connect(database=DATABASE,
                        user=USER,
                        password=PASSWORD,
                        host="localhost",
                        port="5432")
cur = conn.cursor()
