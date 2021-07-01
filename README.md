# MAPD_Project

## Cluster creation
We decided to create a cluster with the five VMs we had at disposition. They are the following:

* MAPD-B_Gr09-5 10.67.22.226
* MAPD-B_Gr09-4 10.67.22.68
* MAPD-B_Gr09-3 10.67.22.63
* MAPD-B_Gr09-2 10.67.22.88
* MAPD-B_Gr09-1 10.67.22.100

In particular, we set the last one as the master node, and the others as pure workers.


### SSH tunneling

```ssh -t -L 8080:localhost:61521 tfaorlin@gate.cloudveneto.it ssh -L 61521:localhost:8080 root@10.67.22.100 ```
