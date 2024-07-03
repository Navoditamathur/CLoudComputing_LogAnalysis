import hashlib
from blockchain import  Blockchain
from db_provider import Server
from data_owner import DataOwner
import merkletools
from adv_client import  MaliciousClient
#This class serves as a query client and also perform verification
class QueryClient:

    def __init__(self, server,blockchain):
        self.server = server
        self.blockchain = blockchain

    #perform query to server
    def query_by_key(self,key):
        return self.server.get_data(key)

    # get proof from server's merkle tree
    def retrieve_verification_path_by_tree(self, key_index):
        if key_index >= 0 and key_index < len(self.server.merkle_tree.leaves):
            return self.server.merkle_tree.get_proof(key_index)
        else:
            print("Invalid node index.")
            return None


    # get merkle root from blockchain
    def retrieve_root_from_blockchain(self):
        return self.blockchain.get_merkle_root()

    # Query clients issue query verifications
    def query_verification(self, retrieved_key, retrieved_value, proofs, root_from_contract):
        hashed_key = hashlib.sha256(str(retrieved_key).encode()).hexdigest()
        hashed_value = hashlib.sha256(str(retrieved_value).encode()).hexdigest()
        concat_hash = hashed_key+hashed_value
        return self.server.merkle_tree.validate_proof(proofs, concat_hash, root_from_contract)













