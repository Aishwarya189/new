from flask import Flask,render_template,request,redirect
from bson.objectid import ObjectId
app=Flask(__name__)
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.camp2016
col=db.usr
@app.route("/")
def create():
     return render_template('home.html')
 



if __name__ == "__main__":
    app.run(debug=True)
