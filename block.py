
class Block:
    def __init__(self, timestamp, nonce, previousHash, transactions):
        self.timestamp = timestamp
        self.nonce = nonce
        self.previousHash = previousHash
        self.transactions = transactions
