from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route("/")

def tasks():
    with open('todo.txt','r') as f:
         todos=f.readlines();
         tasks = []
         for todo in todos:
             todo = todo.split(" ")
             tasks.append(todo)
         return render_template('new.html',todos=tasks)
         
         
@app.route("/create")
def create():
     return render_template('create.html')
     
     
@app.route("/create_task",methods=["post"])
def create_task():
	task_name=request.values.get("task_name")
	task_description=request.values.get("task_description")
	task_date=request.values.get("task_date")
	task_priority=request.values.get("task_priority")
	with open('todo.txt','a') as f:
			f.write(task_name+" "+task_description+" "+task_date+" "+task_priority+"\n")
			return redirect("/")
        
		

if __name__ == "__main__":
    app.run(debug=True)
