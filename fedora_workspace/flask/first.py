class todo:
  def __init__(self,name,description,date,priority):
    self.name=name
    self.description=description
    self.date=date
    self.priority=priority
  def write(self):
     with open("todo.txt","a") as f:
      f.write(name+" "+description+" "+date+" "+priority)
      f.write("\n")
  def read(self):
     with open("todo.txt","r") as f:
      lines= f.readlines()
      for line in lines:
       print(line)
  def search(self):
    name1=raw_input("enter any name")
    with open("todo.txt","r") as f:
        b=f.readlines() 
    for line in b:
        line=line.split(' ')
        if(name1==line[0]):
           print(line)
 
  def delete(self):
    name1=raw_input("enter any name")
    with open("todo.txt","r") as f:
        b=f.readlines() 
    with open("todo.txt","w") as f:
       f.write(" ")
    with open("todo.txt","a") as f:
     for line in b:
       line=line.split(' ')
       if(line!=name1)
         f.write(line)
         print("\n")
      
   
   
    

name=raw_input("enter the task name")
description=raw_input("enter the description")
date=raw_input("enter the date")
priority=raw_input("enter the priority")
Todo=todo(name,description,date,priority)
Todo.write()
Todo.read()
Todo.search()
Todo.delete()
