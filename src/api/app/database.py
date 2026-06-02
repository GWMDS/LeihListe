import os
from sqlmodel import create_engine
from dotenv import load_dotenv

load_dotenv()

db_url = f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ['DB_ADDR']}/lendify"

engine = create_engine(db_url)
