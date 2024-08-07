# Kafka Fraud-Detection System 

## Building A Streaming Fraud Detection System With Kafka and Python
![Screen Shot 2021-12-31 at 4 09 01 PM](https://user-images.githubusercontent.com/70767722/147839040-e395bdd8-1320-4948-ae11-38264656c86f.png)

## Objective:

In this project, I have created my streaming application backed by **Apache Kafka** using a **Python client**. This is a simple **real-time fraud detection system**. I will generate a stream of synthetic transactions and use Python script to process those stream of transactions to detect which ones are legit transaction and the ones that are potential fraud.

## Prerequisites:

Below is the folder map to all the files we have for the project:

```bash
.
├── docker-compose.yml 
├── detector
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── generator
│ ├── Dockerfile
│ ├── app.py
│ ├── transactions.py
│ └── requirements.txt
├── start.sh
├── start_main_docker_compose.sh
├── read_whole_topic.sh
├── restart.sh
├── stop.sh
```

The `generator >> transactions.py` produces fake transactions on one end, filter and log those (`detector >> app.py`) that look suspicious on the other end. This will include:
* a transaction generator (which produces the synthetic data for the process).
* a fraud detector.
Both applications will run in Docker containers and interact with the Kafka cluster.

### Architecture diagram

![Screen Shot 2021-12-31 at 3 57 29 PM](https://user-images.githubusercontent.com/70767722/147838824-3a6cfb90-d06d-4b1a-9daf-10490fa923a4.png)


## The fraud detector mechanism

The fraud detector is a typical example of a stream processing application.
It takes a stream of transactions as an input, performs the filtering task, then outputs the result into two separate streams - those that are legitimate, and those that are suspicious, an operation also known as **branching**.

![Screen Shot 2021-12-31 at 3 57 49 PM](https://user-images.githubusercontent.com/70767722/147838831-f440402a-cabb-4da6-af4b-e5c9e68f9375.png)

**Assumption:**
In the real world, detecting fraud is a complex problem, and it involves various different checks and metrics to tag a transaction as fraud. 
In this project, I will keep the metric simple: it is not legit to transfer more than $900.00 at a time. 
As a result, any transaction whose amount is greater than $900 can be considered fraud. 
For simplifiation purposes, all the transactions are considered to be happening in USD.
![image](https://github.com/user-attachments/assets/2488ef64-6110-4df5-8a6f-27fc4859d7b2)
