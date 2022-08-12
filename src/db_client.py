# blank on purpose - check `final` branch
from functools import lru_cache
import decouple
from pymongo import MongoClient

@lru_cache
def get_db_client():
    mongodb_un = decouple.config("MONGO_INITDB_ROOT_USERNAME")
    mongodb_pw = decouple.config("MONGO_INITDB_ROOT_PASSWORD")
    mongodb_host = decouple.config("MONGO_HOST", default="localhost")
    db_url = f"mongodb://{mongodb_un}:{mongodb_pw}@{mongodb_host}:27017"
    return MongoClient(db_url)