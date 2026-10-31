from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

# Original message
message = b"Hello, this is a digital signature."

# Create message hash
hash_value = SHA256.new(message)

# Sign the message using private key
signature = pkcs1_15.new(private_key).sign(hash_value)

print("Original Message:", message.decode())
print("Digital Signature:", signature.hex())

# Verify signature using public key
try:
    pkcs1_15.new(public_key).verify(
        SHA256.new(message), signature
    )
    print("Signature is valid!")
except (ValueError, TypeError):
    print("Signature is invalid!")
