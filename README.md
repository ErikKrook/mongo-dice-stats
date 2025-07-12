# Simulating Dice Rolls: A Path to the Normal Distribution
This project simulates a simple probabilistic experiment—rolling dice—to demonstrate how the normal distribution emerges from the sum of repeated random events. While the surface-level experiment focuses on statistical behavior, the real goal is to learn and practice MongoDB data pipelines through a staged data engineering process.

## Experiment Overview
We simulate 2,000 rounds of an event where a participant rolls four fair 6-sided dice. The sum of the four dice in each round is recorded. By examining the distribution of these sums, we can observe how the Central Limit Theorem comes into play.

### Project Structure & MongoDB Pipeline
This project follows a basic ETL (Extract, Transform, Load) pattern using MongoDB:

1. simDice.py - Data Simulation (Extract)
Simulates dice rolls from 5 different events (sources).

Generates data in JSON format to mimic event-based data collection.

Each source is treated as a separate dataset.

2. stageDice.py - Load to Staging Collections (Transform)
Loads the JSON data from each source into five different staging collections in MongoDB.

Each collection corresponds to one simulated event source.

3. aggregateDice.py - Aggregation Pipeline (Load)
Uses a MongoDB aggregation pipeline to calculate the sum of the four dice rolls.

Combines and transforms data from staging into a single target collection.

4. analyzeDice.ipynb - Analysis
Analyzes the final aggregated dataset.

Visualizes the distribution of dice sums and explores how closely it resembles a normal distribution.

### Learning Goals
While the statistical analysis is simple, the main objective of this project is to:

Learn how to structure a data pipeline using MongoDB.

Practice working with multiple collections and aggregation pipelines.

Explore the connection between data modeling and statistical concepts.

# Setup Instructions

Create a MongoDB Atlas Cluster and connect to it

Set Up Python Virtual Environment

# Create and activate virtual environment
python -m venv venv
venv/bin/activate 

pip install pymongo pandas matplotlib seaborn notebook dotenv os shutil pymongoarrow json




# Step 1: Simulate and generate data
python simDice.py

# Step 2: Load simulated data to MongoDB staging collections
python stageDice.py

# Step 3: Run the aggregation and load to target collection
python aggregateDice.py

# Step 4: Analyze the results
# Open and run the Jupyter notebook
jupyter notebook analyzeDice.ipynb
