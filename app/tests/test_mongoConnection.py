import os
import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

'''
Testing mongodb connection using ping command. After connection is established the test is passed.
If not test is failed and gives "Connection failed" message. 
After test is done the connection is closed for further use.
'''

class TestMongoDBConnection(unittest.TestCase):
    # setting up the connection
    def setUp(self):
        self.connection_string = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.rzasl.mongodb.net"
        self.client = MongoClient(self.connection_string)

        # testing the mongodb connection
    def test_mongo_connection(self):
        # ping to the mongo db server
        try:
            self.client.admin.command("ping")
            connected = True
        except ConnectionFailure:
            connected = False

        # assert the connection, with "Connection failed" message if connection is false
        self.assertTrue(connected, "Connection failed")

    def tearDown(self):
        # Close the connection after the test is done
        self.client.close()

if __name__ == "__main__":
    unittest.main()

