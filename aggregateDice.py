from pymongo import MongoClient
import os 
from dotenv import load_dotenv 

load_dotenv()  # loads the .env file

mongo_uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(mongo_uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Our staging area
staging_area = client["dice_staging"]

# Our target area
target_area = client["dice_analytics"]

# The fileds we want to project
project = {
    "$project": {
        "_id":1,
        "primary_key": 1,
        "event": 1,
        "sum_of_rolls": { "$sum": "$dice_rolls" },
        "count_of_rolls": { "$size": "$dice_rolls" }
        }
    }

# The collection we want to write to
merge = {
    "$merge": {
        "into": {
            "db": "dice_analytics",
            "coll": "all_rolls"
        },
        "on": "_id",
        "whenMatched": "merge",  # update existing
        "whenNotMatched": "insert"  # insert new
    }
}

pipeline = [project, merge]

# List of all the events
events = ["swe", "den", "nor", "fin", "ice"]

for event in events:

    collection = f"{event}_rolls"

    staging_area[collection].aggregate(pipeline)
    
    print(f"Aggregation complete. Results written to dice_analytics.all_rolls from dice_staging.{collection}.")

# Close the connection
client.close()
