from block import Block
from transaction import Transaction
from datetime import datetime

if __name__ == "__main__":
    b = Block(datetime.now(), 0, '', [])
    b.transactions.append(Transaction('prev', 'recipient', 123.45))
    print(b.hash())
