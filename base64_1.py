import json
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Path to your service account JSON file
service_account_path = './a.json'

# Load the JSON data and extract the private key
with open(service_account_path, 'r') as file:
    data = json.load(file)

# Extract the raw private key from the JSON file
raw_private_key = data['private_key']

# Load the private key using cryptography
private_key = serialization.load_pem_private_key(
    raw_private_key.encode(),
    password=None,
    backend=default_backend()
)

# Convert the private key to PKCS#8 DER format
pkcs8_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Encode the PKCS#8 private key in base64 for use in environment variables
pkcs8_base64 = base64.b64encode(pkcs8_private_key).decode('utf-8')

# Output the base64-encoded PKCS#8 private key
print("Base64 Encoded PKCS#8 Private Key:")
print(pkcs8_base64)
