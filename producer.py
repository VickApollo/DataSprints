import os
import json
from kafka import KafkaProducer

# Pointing the current working directory to iterate over files 
cwd = os.path.dirname(__file__)
sources = [ "data-sample_data-nyctaxi-trips-2009-json_corrigido.json",
            "data-sample_data-nyctaxi-trips-2010-json_corrigido.json",
            "data-sample_data-nyctaxi-trips-2011-json_corrigido.json",
            "data-sample_data-nyctaxi-trips-2012-json_corrigido.json"]

# Initialize the Producer (Sender)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Reading each file at a time
for file in sources:
    f = os.path.join(cwd , "DATA", file)                      # Pointing to file path
    for ix , line in enumerate(open(f , 'r').readlines()):    # Reading lines (Simulating Requests) 
        if ix <= 10:                                          # Filtering only the first 10 lines (to see all, put >= 0)
            content = line.encode('utf-8')                    # Passing Byte format (Required by kafka)
            producer.send(topic='DataSprint', value=content)  # Send message
