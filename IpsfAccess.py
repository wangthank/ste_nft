import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()
PINATA_API_KEY = "7284e7650556c1e6ee48"
PINATA_SECRET_API_KEY = "bd1b54933a1b9b8248761ed1a1bbff1f713bb13c2f8a2b29c1167f8ea920a7"

json_headers = {
    "Content-Type": "application/json",
   # "pinata_api_key"= "7284e7650556c1e6ee48",
   # "pinata_secret_api_key": os.getenv("bd1b54933a1b9b8248761ed1a1bbff1f713bb13c2f8a2b29c1167f8ea920a717"),
    "pinata_api_key": ("4e3e67d89a87ec2d6dc1"),
    "pinata_secret_api_key": ("cb16ac925fe8882ab69a5aa1de60d28d358b1eed840eb78c0ee4addaaef4a4a8"),
}

file_headers = {
   # "pinata_api_key": os.getenv("7284e7650556c1e6ee48"),
   # "pinata_secret_api_key": os.getenv("bd1b54933a1b9b8248761ed1a1bbff1f713bb13c2f8a2b29c1167f8ea920a717"),
    "pinata_api_key": ("4e3e67d89a87ec2d6dc1"),
    "pinata_secret_api_key": ("cb16ac925fe8882ab69a5aa1de60d28d358b1eed840eb78c0ee4addaaef4a4a8"),
}

def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)

def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash

def pin_json_to_ipfs(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json,
        headers=json_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
"""
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")

json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET_API_KEY,
}

file_headers = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET_API_KEY,
}

def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)

def pin_file_to_ipfs(file_path):
    with open(file_path, 'rb') as file_data:
        r = requests.post(
            "https://api.pinata.cloud/pinning/pinFileToIPFS",
            files={'file': file_data},
            headers=file_headers
        )
        if r.status_code != 200:
            print(f"Error: Received status code {r.status_code}")
            print(r.text)
            return None

        try:
            response_json = r.json()
            print(response_json)  # In ra JSON response để kiểm tra
            ipfs_hash = response_json["IpfsHash"]
            return ipfs_hash
        except KeyError:
            print("Error: 'IpfsHash' not found in response")
            print(response_json)
            return None
        except ValueError:
            print("Error: Unable to parse JSON response")
            print(r.text)
            return None

def pin_json_to_ipfs(json_data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json_data,
        headers=json_headers
    )
    if r.status_code != 200:
        print(f"Error: Received status code {r.status_code}")
        print(r.text)
        return None

    try:
        response_json = r.json()
        print(response_json)  # In ra JSON response để kiểm tra
        ipfs_hash = response_json["IpfsHash"]
        return ipfs_hash
    except KeyError:
        print("Error: 'IpfsHash' not found in response")
        print(response_json)
        return None
    except ValueError:
        print("Error: Unable to parse JSON response")
        print(r.text)
        return None

# Ví dụ sử dụng
file_path = "path_to_your_file"
json_content = {"key": "value"}

# Pin file to IPFS
file_ipfs_hash = pin_file_to_ipfs(file_path)
if file_ipfs_hash:
    print(f"File IPFS Hash: {file_ipfs_hash}")

# Pin JSON to IPFS
json_ipfs_hash = pin_json_to_ipfs(convert_data_to_json(json_content))
"""
