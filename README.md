# MAPD_Project

## Cluster creation
We decided to create a cluster with the five VMs we had at disposition. They are the following:

* MAPD-B_Gr09-5 10.67.22.226

* MAPD-B_Gr09-4 10.67.22.68
* MAPD-B_Gr09-3 10.67.22.63

* MAPD-B_Gr09-2 10.67.22.88

* MAPD-B_Gr09-1 10.67.22.100

In particular, we set the last one as the master node, and the others as pure workers.

## Cluster connection

Once a master is deployed in the master VM with  ```./start-master.sh ```, its Web-UI can be accessed at localhost:8080 via double SSH port forwarding using the following command

```ssh -t -L 8080:localhost:61521 tfaorlin@gate.cloudveneto.it ssh -L 61521:localhost:8080 root@10.67.22.100```

To interact with the cluster and work at the project we also forward to our local machine a Jupyter notebook hosted at port 8888 in the master VM

 ```ssh -t -L 8888:localhost:8888  tfaorlin@gate.cloudveneto.it ssh -L 8888:localhost:8888 root@10.67.22.100```

 ```jupyter notebook --port 8888 --no-browser --allow-root```

In the end, we visit all the nodes and start all the workers with

 ```/home/packages/spark-3.1.2-bin-hadoop3.2/sbin/start-worker.sh spark://10.67.22.100:7077```
 
 To start the Kafka server type in order
 
 ```/home/packages/kafka_2.13-2.7.0/bin/zookeeper-server-start.sh /home/packages/kafka_2.13-2.7.0/config/zookeeper.properties```
 
  ```/home/packages/kafka_2.13-2.7.0/bin/kafka-server-start.sh /home/packages/kafka_2.13-2.7.0/config/server.properties ```
