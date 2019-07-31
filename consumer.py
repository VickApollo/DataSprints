import time
import json
from kafka import KafkaConsumer

# Variables need for average calculation
total = 0
amount = 0

# Initialize Consumer (Agent)
consumer = KafkaConsumer(bootstrap_servers="localhost:9092")

# Configuring to our consumer only listenings to DataSprint Topic
consumer.subscribe(['DataSprint'])

# Listening...
for msg in consumer:
    val = json.loads(msg.value)                      # Loading content from streaming in a json format
    if val.get("passenger_count") <= 2:              # Check the passenger count (only calculate if there is no more the 2 people)
        total += val.get("trip_distance")            # Summing trip distances
        amount += 1                                  # Counting trips
        mean = total / amount                        # Calculate Average Distance
    print("Average Trip Distance: {}".format(mean))  # Perform the mean calc and print the result
    time.sleep(0.3)                                  # Delaying the requests is not required, i'm only doing it to reduce performance issues of my personal machine
    
