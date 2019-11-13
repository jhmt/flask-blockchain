from block import Block
from transaction import Transaction

class Blockchain:
    
    def __init__(self, blockchain_address):
        block = Block(datetime.now(), 0, '', [])
        self.create_block(0, block.hash())
        self.blockchain_address = blockchain_address
        self.chain = []

    def create_block(self, nonce, previous_hash):
        block = Block(nonce, previous_hash, self.transactionPool)
        self.chain.append(block)
        self.transactionPool = []
        return block

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, value):
        new_transaction = Transaction(sender, recipient, value)

    def mining(self):
        return True

    def calc_total_amount(self, blockchain_address):
        total_amount = 0.0
        for block in self.chain:
            for t in block.transactions:
                value = t.value
                if blockchain_address == t.recipient_blockchain_address:
                    total_amount += value
                
                if blockchain_address == t.sender_blockchain_address:
                    total_amount -= value

        return total_amount
