import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
user_name = os.getenv('MONGODB_USERNAME')
user_password = os.getenv('MONGODB_PASSWORD')
mongo_uri = f"mongodb+srv://{user_name}:{user_password}@cluster0.rzasl.mongodb.net"
client = MongoClient(mongo_uri)
db = client.shop_db
products_collection = db.products

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)