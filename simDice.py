import random
import pandas as pd
import os
import shutil



# List of event tags
events = ["swe", "den", "nor", "fin", "ice"]

# Loop over each event
for event in events:

    dataset = []

    # Simulate tests (dice rolls) per event
    for test in range(3):
        # Generate 4 random dice rolls (1-6)
        dice_rolls = [random.randint(1, 6) for _ in range(4)]

        # Create a unique primary key for each test
        primary_key = f"{event}_{test}"

        # Construct the document with the required fields
        
        dataset.append({
            "primary_key": primary_key,
            "event": event,
            "dice_rolls": dice_rolls
            })

        # Add the document to the dataset list
        

    # Convert list of dicts to an Arrow Table using the predefined schema
    df = pd.DataFrame(dataset)

    event_folder = f"{event}_dataset"

    # Define output directory in the current folder
    output_dir = os.path.join(os.getcwd(), event_folder)  

    # Remove folder if it already exits
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Create a new folder for our dataset 
    os.makedirs(output_dir, exist_ok=True)

    event_dataset = f"{event_folder}/{event}_data.json"

    # Set our primary key as index
    df.set_index('primary_key', inplace=True)
    # Write to JSON dataset 
    df.to_json(event_dataset, orient='table', indent=4)


    print(f"Dataset written to: {output_dir}")


