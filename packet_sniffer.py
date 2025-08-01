import time
import boto3
from scapy.all import sniff, wrpcap

# ------------------------
# Configuration
# ------------------------

# Duration for capturing network traffic (in seconds)
capture_duration = 15  

# Output filename with timestamp
current_time = time.strftime("%Y%m%d-%H%M%S")
output_file = f"network_traffic_{current_time}.pcap"

# AWS S3 bucket details (use environment config or placeholder keys)
aws_access_key_id = "access-key-id"
aws_secret_access_key = "secret-access-key"
bucket_name = "bucket-name"

# ------------------------
# Packet Capture Function
# ------------------------

def capture_traffic(duration, output_file):
    print(f"[*] Starting packet capture for {duration} seconds...")
    packets = []

    end_time = time.time() + duration
    while time.time() < end_time:
        packets.append(sniff(count=1)[0])

    wrpcap(output_file, packets)
    print(f"[+] Capture complete. Saved to: {output_file}")

# ------------------------
# Upload to AWS S3 Function
# ------------------------

def upload_to_s3(file_path, bucket_name):
    print(f"[*] Uploading {file_path} to S3 bucket: {bucket_name} ...")
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        s3_client.upload_file(file_path, bucket_name, file_path)
        print("[+] File successfully uploaded to S3.")
    except Exception as e:
        print(f"[!] Upload failed: {e}")

# ------------------------
# Main Execution
# ------------------------

if __name__ == "__main__":
    capture_traffic(capture_duration, output_file)
    upload_to_s3(output_file, bucket_name)