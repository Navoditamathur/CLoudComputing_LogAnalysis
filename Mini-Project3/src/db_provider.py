from cassandra.cluster import Cluster
import hashlib
import json
import copy
class Server:
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.merkle_tree = None
        self.keyspace = "mini_project_3"  # keyspace(database) name for storing data
        self.table = "kv_data" # table name for storing data

        # Create keyspace and corresponding table
        self.session.execute(
            "CREATE KEYSPACE IF NOT EXISTS " + self.keyspace + " WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};")
        self.session.set_keyspace(self.keyspace)
        self.session.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (key text PRIMARY KEY, value text);")


    # Use insert syntax to add new key value pair to the target table
    def add_data(self, key, value):
        self.session.execute(f"INSERT INTO {self.table} (key, value) VALUES ('{key}', '{value}')")
        if self.merkle_tree:
            self.merkle_tree.reset_tree()
            data = self._get_all()
            for k,v in sorted(data):
                hashed_key = hashlib.sha256(str(k).encode()).hexdigest()
                hashed_value = hashlib.sha256(str(v).encode()).hexdigest()
                concat_hash = hashed_key+hashed_value
                self.merkle_tree.add_leaf(concat_hash)
            self.merkle_tree.make_tree()

    def _get_all(self):
        return self.session.execute(f"SELECT * FROM {self.table}").all()

    # Retrieve value by key
    def get_data(self, key):
        return self.session.execute(f"SELECT value FROM {self.table} WHERE key = '{key}'").one()[0]

