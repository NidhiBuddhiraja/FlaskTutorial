from flask import Flask,request,jsonify;
from dotenv import load_dotenv;
from pymongo.mongo_client import MongoClient;
import os;

load_dotenv();

uri = os.getenv('uri');

# Create a new client and connect to the server
client = MongoClient(uri,connect=False);
db=client.Test;
collection = db['flask-tutorial'];

app = Flask(__name__);

# How to send data from front end to backend
# 1st way AJAX Queries

# 2nd way Basic HTML Form 
# Upload data to the database
@app.route('/')
def home():
    return "Welcome to Flask's backend api";

@app.route('/submit',methods = ["POST"])
def submit():
    
    form_data = dict(request.json);

    # insert into document
    collection.insert_one(form_data);

    return "Data Submitted Successfully";

@app.route('/view')
def view():
    data = collection.find();
    data = list(data);

    for item in data:
        print(item);
        del item['_id'];
    
    print(data);
    
    data = {
        'data':data
    };
    return jsonify(data);

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True); 