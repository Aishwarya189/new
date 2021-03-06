from flask import Flask,render_template,request,redirect
from bson.objectid import ObjectId
app=Flask(__name__)
from pymongo import MongoClient
import json

client=MongoClient('localhost',27017)
db=client.camp2016
todos=db.todo

@app.route("/")
def tasks():
	tasks=todos.find()
	tasks=list(todos.find())
	tasks=str(tasks)
	return json.dumps(tasks)
	
@app.route("/create")
def create():
     return render_template('create.html')

@app.route("/create_task",methods=["post"])
def create_task():
	task_name=request.values.get("task_name")
	task_description=request.values.get("task_description")
	task_date=request.values.get("task_date")
	task_priority=request.values.get("task_priority")
	todos.insert({"name":task_name,"description":task_description,"date":task_date,"priority":task_priority})
	for todo in todos.find():
		print todo
	return redirect("/")

@app.route("/delete")
def delete():
	id=request.values.get("id")
	todos.remove({"_id":ObjectId(id)})
	return redirect("/")
@app.route("/update")
def update():
	id=request.values.get("id")
	task=todos.find({"_id":ObjectId(id)})
	return render_template('update.html',tod=task)
@app.route("/update_task")
def update_task():
	id=request.values.get("id")
	nam=request.values.get("task_name")
	des=request.values.get("task_description")
	dat=request.values.get("task_date")
	prior=request.values.get("task_priority")
	todos.update({"_id":ObjectId(id)},{'$set':{"name":nam,"description":des,"date":dat,"priority":prior}})
	return redirect("/")
		
@app.route("/search")
def search():
		return render_template('search1.html')

@app.route("/search_task")
def search_task():
	sel=request.values.get("sel")
	key=request.values.get("ip")
	todos_s=todos.find({sel:key})
	return render_template('print.html',res=todos_s)
	return redirect("/")	

if __name__ == "__main__":
    app.run(debug=True)
