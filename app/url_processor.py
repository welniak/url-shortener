import base64
import hashlib
import app.database as db
from typing import Union

def create_and_store_hash(url: str) -> str:
    url_hash = _create_hash_from(input_string=url)
    db.store_url(url=url, hash=url_hash)
    return url_hash

def get_url_for_hash(hash: str) -> Union[str, None]:
    return db.read_url(hash)

def _create_hash_from(input_string: str, length: int=8) -> str:
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the input string
    sha256.update(input_string.encode('utf-8'))
    
    # Get the digest and encode it in base64
    digest = sha256.digest()
    b64_encoded = base64.urlsafe_b64encode(digest)
    
    # Return the first 'length' characters
    return b64_encoded[:length].decode('utf-8')
