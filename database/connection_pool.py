from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv
import os
from contextlib import contextmanager

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

try:
    pool = SimpleConnectionPool(minconn=1, maxconn=5,
                            host= HOST,
                            database=DBNAME,
                            user=USER,
                            password=PASSWORD,
                            port=PORT)

except Exception as e:
    print(f"Failed to connect to database: {e}")

@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)
