'''#!/bin/python3

from Cryptodome.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import rsa

publicKey = RSA.import_key(open("./machine1/ex_ftp/key.pub", "r").read())
privateKey = RSA.import_key(open("./machine1/ex_ftp/key.priv", "r").read())
message = b"\x00"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
pricKey = PKCS1_OAEP.new(publicKey)
encrypted = pricKey.encrypt(message)

print(encrypted)'''

'''from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Load the RSA public key from a PEM file
with open('./machine1/ex_ftp/key.pub', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Message to be encrypted
message = b'This is a message to be encrypted'

# Encrypt the message
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print the encrypted data (in bytes format)
print("Encrypted data:", ciphertext)''''''
