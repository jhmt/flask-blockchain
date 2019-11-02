from block import Block
from datetime import datetime

if __name__ == "__main__":
    b = Block(datetime.now(), 0, '', [])
    b.hash()
