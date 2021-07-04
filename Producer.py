from kafka.admin import KafkaAdminClient
from kafka import KafkaProducer

import os
import ssl
import json
import time
import pandas as pd


ssl._create_default_https_context = ssl._create_unverified_context

KAFKA_BOOTSTRAP_SERVERS = '10.67.22.100:9092'
kafka_admin = KafkaAdminClient(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
)

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

for i in range(0, 81):
    i = str(i).zfill(2)
    url = f"https://cloud-areapd.pd.infn.it:5210/swift/v1/AUTH_d2e941ce4b324467b6b3d467a923a9bc/MAPD_miniDT_stream/data_0000{i}.txt"
    df = pd.read_csv(url)
    for j in range(0, df.shape[0]):
        jj = df.iloc[j].to_dict()
        for key in ['HEAD', 'FPGA', "TDC_CHANNEL", "ORBIT_CNT", "BX_COUNTER"]:
            jj[key] = int(jj[key])
        producer.send('topic_stream', json.dumps(jj).encode('utf-8'))
        time.sleep(0.01)
    producer.flush()
