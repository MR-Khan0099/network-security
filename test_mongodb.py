
from pymongo.mongo_client import MongoClient
import os
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("MONGO_DB_URL")

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)