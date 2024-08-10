import base64
import hashlib

def create_hash_from(url) -> str:
    return _custom_length_hash(input_string=url, length=8)

def _custom_length_hash(input_string, length=16) -> str:
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the input string
    sha256.update(input_string.encode('utf-8'))
    
    # Get the digest and encode it in base64
    digest = sha256.digest()
    b64_encoded = base64.urlsafe_b64encode(digest)
    
    # Return the first 'length' characters
    return b64_encoded[:length].decode('utf-8')
