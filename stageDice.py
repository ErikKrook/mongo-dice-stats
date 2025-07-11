from pymongo import MongoClient
import os 
from dotenv import load_dotenv 
import pandas as pd
from pymongoarrow.api import write
import json
from pymongoarrow.monkey import patch_all

load_dotenv()  # loads the .env file

mongo_uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(mongo_uri)

# Our staging area
staging_area = client["dice_staging"]

patch_all()

# List of all the events
events = ["swe", "den", "nor", "fin", "ice"]

for event in events:

    # Create the collection name for the event
    collection = f"{event}_rolls"
    
    # File to the dataset for the event
    file = f"{event}_dataset/{event}_data.json"

    # Load JSON file
    with open(file, "r") as f:
        data = json.load(f)  

    # convert to DataFrame 
    df = pd.DataFrame(data["data"])

    # Truncate the staging table before inserting

    staging_area[collection].delete_many({})    

    # Insert with pymongoarrow
    write(staging_area[collection], df)

    print(f"Data inserted successfully into {collection}")

# Close the connection
client.close()

