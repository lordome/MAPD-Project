from kafka.admin import KafkaAdminClient
from kafka import KafkaProducer

import os
import ssl
import json
import time
import pandas as pd
from tqdm import tqdm

#SSL context to dowload without errors data from the given server
ssl._create_default_https_context = ssl._create_unverified_context

#Creating KAFKA_BOOTSTRAP_SERVER environmental variable
KAFKA_BOOTSTRAP_SERVERS = '10.67.22.226:9092'
kafka_admin = KafkaAdminClient(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
)

#Creating a producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

#Partition number
n_part = 4
curr_part = 0

for i in range(0, 81):
    #Dowloading data from server
    i = str(i).zfill(2)
    url = f"https://cloud-areapd.pd.infn.it:5210/swift/v1/AUTH_d2e941ce4b324467b6b3d467a923a9bc/MAPD_miniDT_stream/data_0000{i}.txt"
    df = pd.read_csv(url)
    
    #Removing possible outliers
    df = df[df.ORBIT_CNT < 5e8]
    print(f"Reading file data_0000{i}.txt")
    
    #For loop over file size
    for j in tqdm(range(0, df.shape[0])):
        #Creating dictionaries from dataframe's rows
        jj = df.iloc[j].to_dict()
        #Trasforming the unnecessary floats into ints
        for key in ['HEAD', 'FPGA', "TDC_CHANNEL"]:
            jj[key] = int(jj[key])
        #Sending the json row to the Kafka topic with a different partition for each iteration
        producer.send('topic_stream', json.dumps(jj).encode('utf-8'), partition = curr_part)
        curr_part = (curr_part+1)%n_part
        time.sleep(0.0003)
    producer.flush()
