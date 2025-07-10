import random
import pyarrow as pa
import pyarrow.dataset as ds
import os
import shutil

# Define the Arrow schema: primary_key and event are strings, dice_rolls is a list of integers
schema = pa.schema([
    ("primary_key", pa.string()),
    ("event", pa.string()),
    ("dice_rolls", pa.list_(pa.int64()))
])

# List of event tags
events = ["swe", "den", "nor", "fin", "ice"]

# Loop over each event
for event in events:
    dataset = []  # Container to hold all documents for this event

    # Simulate tests (dice rolls) per event
    for test in range(3):
        # Generate 4 random dice rolls (1-6)
        dice_rolls = [random.randint(1, 6) for _ in range(4)]

        # Create a unique primary key for each test
        primary_key = f"{event}_{test}"

        # Construct the document with the required fields
        document = {
            "primary_key": primary_key,
            "event": event,
            "dice_rolls": dice_rolls
        }

        # Add the document to the dataset list
        dataset.append(document)

    # Convert list of dicts to an Arrow Table using the predefined schema
    table = pa.Table.from_pylist(dataset, schema=schema)

    event_dataset = f"{event}_dataset"

    # Define output directory in the current folder
    output_dir = os.path.join(os.getcwd(), event_dataset)  

    # Remove folder if it already exits
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Create a new folder for our dataset 
    os.makedirs(output_dir, exist_ok=True)

    # Write to Parquet dataset 
    ds.write_dataset(
        table,
        base_dir=output_dir,
        format="parquet"
    )

    print(f"Dataset written to: {output_dir}")

