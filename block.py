import json
import hashlib

class Block:
    def __init__(self, timestamp, nonce, previous_hash, transactions):
        self.timestamp = timestamp
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.transactions = transactions
    
    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True, default=str)

    def hash(self):
        return hashlib.sha256(self.to_json().encode()).hexdigest()

