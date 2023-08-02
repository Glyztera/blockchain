import hashlib
import json
from urllib.parse import urlparse

def hash(block):
    """
    Creates a SHA-256 hash of a Block

    :param block: Block
    """
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def valid_proof(last_proof, proof, last_hash):
    """
    Validates the Proof

    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :param last_hash: <str> The hash of the Previous Block
    :return: <bool> True if correct, False if not.
    """
    guess = f'{last_proof}{proof}{last_hash}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

def parse_url(address):
    """
    Parse the URL to extract the netloc or path

    :param address: Address of node. Eg. 'http://192.168.0.5:5000'
    :return: netloc or path or raise ValueError
    """
    parsed_url = urlparse(address)
    if parsed_url.netloc:
        return parsed_url.netloc
    elif parsed_url.path:
        return parsed_url.path
    else:
        raise ValueError('Invalid URL')
