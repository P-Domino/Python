import hashlib as hl
import json

def hashString256(string):
    return hl.sha256(string).hexdigest()


def hashBlock(block):
    """Hashes a block and returns a string representation of it.
    
    Arguments:
        :block: The block that should be hashed.
    """
    return hl.sha256(json.dumps(block, sortKeys = True).encode()).hexdigest()