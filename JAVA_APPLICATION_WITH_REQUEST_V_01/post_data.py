import requests
import time

API = "http://<IP_ADDRESS>:30007/api/upload"

for i in range(30):
    data = {
        "field1": f"Test data {i+1}",
        "field2": f"More test data {i+1}"
    }

    response = requests.post(API, json=data)
    print(f"[{i+1}] Status: {response.status_code} | Response: {response.text}")
    time.sleep(2)

