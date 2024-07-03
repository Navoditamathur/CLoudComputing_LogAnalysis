from db_provider import Server
import hashlib
import merkletools

class DataOwner:
    #init data owner with the key value data
    #specify the server object
    def __init__(self,key_value_data,server,blockchain):
        self.data= key_value_data
        self.server= server
        self.merkle_tree = None
        self.blockchain = blockchain

    #insert data to self.server
    def insert_data_to_server(self):
        for key, value in sorted(self.data.items()):
            self.server.add_data(key, value)

    # build merkle tree on data owner side to get the merkle root, key+value as values
    # You can use functions provided by merkletools
    def build_merkle_tree(self):
        mt = merkletools.MerkleTools()
        for key, value in sorted(self.data.items()):
            hashed_key = hashlib.sha256(str(key).encode()).hexdigest()
            hashed_value = hashlib.sha256(str(value).encode()).hexdigest()
            mt.add_leaf(hashed_key + hashed_value)
        mt.make_tree()
        self.merkle_tree = mt


    # upload self.merkle_tree to self.server
    def upload_merkle_tree_to_server(self):
        if self.merkle_tree:
            self.server.merkle_tree = self.merkle_tree


    # get merkle root from self.merkle_tree
    def get_merkle_root(self):
        return self.merkle_tree.get_merkle_root()

    #upload merkle root to self.blockchains
    def upload_merkle_root_to_blockchain(self):
        merkle_root = self.get_merkle_root()
        self.blockchain.set_merkle_root(merkle_root)






