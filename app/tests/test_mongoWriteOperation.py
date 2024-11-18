import os
import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

'''
Testing mongodb write operation. After the sample document is inserted, upon success it returns the id to the response.
This id is being tested here for the none value. After that db is being queried using same id and value is tested with 
the original document value. Best practice is to use test db so that it does not affect the real data for test data. After 
 test is done the db is dropped and connection is closed'''

class TestMongoDBWriteOperation(unittest.TestCase):
    # setting up the connection
    def setUp(self):
        self.connection_string = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.rzasl.mongodb.net"
        self.client = MongoClient(self.connection_string)
        self.db = self.client["test_db"]  # Creating a test database inside mongodb atlas
        self.collection = self.db["test_product"]  # Creating a test product collection inside database

    def test_insert_document(self):
        # creating sample test product
        test_product = {
        "name": "Diamond Necklace",
        "image_path": "../static/images/product1.jpg",
        "price": 69.99,
        "tag": "Necklace" }

        # insert product to the database
        insert_response = self.collection.insert_one(test_product)

        # check if the response is none or not. After data is successfully inserted it returns the data with id
        self.assertIsNotNone(insert_response.inserted_id, "Insertion failed.....")

        # querying to the inserted document
        query_response = self.collection.find_one({"_id": insert_response.inserted_id})
        # check if the response match with test_product
        self.assertEqual(test_product["name"], query_response["name"])
        self.assertEqual(test_product["image_path"], query_response["image_path"])
        self.assertEqual(test_product["price"], query_response["price"])
        self.assertEqual(test_product["tag"], query_response["tag"])

    def tearDown(self):
        # Drop the test collection after the test is done
        self.collection.drop()
        # Close the MongoDB connection
        self.client.close()

if __name__ == "__main__":
    unittest.main()

