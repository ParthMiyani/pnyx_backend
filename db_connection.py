from dotenv import load_dotenv
import psycopg2
import os

def get_db_connection():
    try:
        load_dotenv('.env.local')
        conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'],
                            database=os.environ['POSTGRES_DATABASE'],
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])
        return conn
    except Exception as e:
        print("Database connection failed: ", e)
        return None