# Module 1 - Create a Blockchain

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0') # Common practice is 0

    def create_block(self, proof, previous_hash):

        # Create a new block
        block={'index' : len(self.chain) + 1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash}
                self.chain.append(block)
                return block
        # Retrieve last block in list
        def get_previous_block(self):
            return self.chain[-1]

# Part 2 - Mining our blockchain


