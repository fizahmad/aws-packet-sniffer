# Packet Sniffer Tool

This Python tool captures live network packets and uploads them to an AWS S3 bucket. Designed as a hands-on security lab task to simulate secure cloud storage of traffic logs.

## Features
- Captures network traffic using `scapy`
- Automatically stops capture after a preset time
- Saves traffic to a `.pcap` file
- Uploads the file to a specified S3 bucket using `boto3`

## Requirements
- Python 3.x
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [scapy](https://scapy.readthedocs.io/en/latest/)

Install with:
```bash
pip install boto3 scapy
```

## Usage Demo
Demonstration of capturing packets and uploading logs to AWS S3.

https://github.com/user-attachments/assets/16bab140-25a1-47f3-97f6-eacb03a59bae
