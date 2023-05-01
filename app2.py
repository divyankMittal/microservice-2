from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import pymongo


   
   
 


app = Flask(__name__)

@app.route("/submit" , methods=['POST','GET'])
def func():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['divyank']
    collection = db['mySampleCollection']
    if request.method=="POST":
       name = request.form['fname']
       sport = request.form['lname']
       dictionary = {'name' : name, 'sport' : sport}
       collection.insert_one(dictionary) 
       return render_template("index1.html")
 
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)