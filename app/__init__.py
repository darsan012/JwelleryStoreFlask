import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

''' Getting necessary variables from .env '''
user_name = os.getenv('MONGODB_USERNAME')
user_password = os.getenv('MONGODB_PASSWORD')
mongo_uri = f"mongodb+srv://{user_name}:{user_password}@cluster0.rzasl.mongodb.net"

client = MongoClient(mongo_uri) # creating mongo db client
db = client.shop_db # shop_db is the name of the database in mongodb atlas
products_collection = db.products # products is the name of the collection inside the database

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)