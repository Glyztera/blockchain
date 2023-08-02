#Generate Keys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

# Serialize the keys for storage or transmission
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

#Sign with Keys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

# Sample transaction data as a string
transaction = "sender:receiver:amount"

signature = private_key.sign(transaction.encode(), ec.ECDSA(hashes.SHA256()))


#Verfy Transaction/Signage
try:
    public_key.verify(signature, transaction.encode(), ec.ECDSA(hashes.SHA256()))
    print("Valid Signature!")
except InvalidSignature:
    print("Invalid Signature!")
