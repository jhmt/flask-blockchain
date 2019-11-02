import json
import hashlib

class Block:
    def __init__(self, timestamp, nonce, previousHash, transactions):
        self.timestamp = timestamp
        self.nonce = nonce
        self.previousHash = previousHash
        self.transactions = transactions
    
    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True, default=str)

    def hash(self):
        return hashlib.sha256(self.to_json().encode()).hexdigest()

