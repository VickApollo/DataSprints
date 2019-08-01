#  Amazon EC2

First, go to aws console and create your account: https://aws.amazon.com/pt/console/

1. Let's start an EC2 instance. Go on Services panel and click on EC2.

2. Chose the instance **ami-02f706d959cedf892**. It's an Amazon Linux with Fedora distribution.

3. Press **Review and Launch**. We don't have to change anything on this instance.

4. When comes the screen about key access chose **Create a New Key Pair** and save the key onto your computer (remeber where you save it, you are going to need those keys everytime you want to access).

5. Now your instance is up and running.

   

We are going to access the server through ssh. To do that, open your terminal (assuming you have linux O.S.) go to the directory where you download the pen key. For me the file is called DataSprint.pem.txt.

```shell
chmod 400 DataSprint.pem.txt
ssh -i DataSprint.pem.txt ec2-user@ec2-13-59-151-83.us-east-2.compute.amazonaws.com
```



# KAFKA



## Download & Installing

First, let's ensure that we are using Java 1.8

to check, run the following command:

```shell
java -version
```

If you need to install, run the following command

```shell
sudo yum install java-1.8.0-openjdk.x86_64
```

Download Kafka

```shell
cd /usr/src
wget http://apache.mirror.vexxhost.com/kafka/2.2.0/kafka_2.12-2.2.0.tgz
tar -xzf kafka_2.12-2.2.0.tgz
cd kafka_2.12-2.2.0
```

t's create some environment variables

```shell
sudo vi /etc/profile
```

Add the following enviroment variables: JAVA_HOME and JRE_HOME 

```shell
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
export JRE_HOME=/usr/lib/jvm/jre
export KAFKA_HOME=/usr/src/kafka_2.12-2.2.0
```

Let's environment resources by setting the maximum amount of memory for Kafka (JVM).

To do that, go to bin directory inside kafka root directory

```shell
cd $KAFKA_HOME/bin
```

After that, open tkafka-server-start.sh

```shell
sudo vi kafka-server-start.sh
```

Locate heap configuration and set the maximum  memory for 256M and minimum for 126M 

```shell
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
```

Save the file.

```shell
cd $KAFKA_HOME
```



## Starting Services

To start zookeeper, go to kafka directory and type the following command

```shell
bin/zookeeper-server-start.sh config/zookeeper.properties &
```

After that we are ready to start kafka…  kafka main directory, type the following commands

```shell
bin/kafka-server-start.sh config/server.properties &
```



## Testing Kafka

Before testing, let's create a topic. 

```shell
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic DataSprint
```



Let's send a message to test if our service is running correctly 

```shell
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic DataSprint
```



Send any messages you want. After that (or at the same time in another terminal), let's retrieve the messages. 

```shell
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic DataSprint --from-beginning
```

Everything working? Ok. Let's close all terminals for now. Time for some logic.



# Python (Kafka Module)

For this project we are not going to use the default version of python that comes on servers. For compatibilities we are going to use python 3.6.

Open terminal and type the following command:

```shell 
yum install python3.6
```



## Kafka Module Installation

To install is very simple:

```shell
pip-3.6 install kafka
```



## IMPLEMETATION

Weare going to need 2 files:

1. consumer.py 
2. producer.py

Both are going to extend intefaces from Kafka module.



code from consumer.py

```python
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
```



 

code from producer.py

```python
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
```



# Running Everything

We are going to need 4 terminals to do this test

First terminal: Starting Zookeeper

```shell 
cd $KAFKA_HOME
bin/zookeeper-server-stop.sh    # Just to ensure that are no instances running
bin/zookeeper-server-start.sh config/zookeeper.properties &
```



Second terminal: Starting Kafka

```shell 
bin/kafka-server-stop.sh    # Just to ensure that are no instances running
bin/kafka-server-start.sh config/server.properties &
```



Third terminal: running consumer.py

```shell 
cd `go to your files directory`    # For me the path is on desktop/project
python consumer.py
```



Second terminal: Starting Kafka

```shell 
python producer.py
```

Watch the magic happening on consumer.py screen! That's it!