class Transaction:
    def __init__(self,
    sender_blockchain_address,
    recipient_blockchain_address,
    value):
        self.sender_blockchain_address = sender_blockchain_address
        self.recipient_blockchain_address = recipient_blockchain_address
        self.value = value
