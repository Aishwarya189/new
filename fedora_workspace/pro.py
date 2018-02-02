class todo:
	name= raw_input("enter the task name")
	description=raw_input("enter the description")
	date=raw_input("enter the due date")
	priority=raw_input("enter the priority")
        def __init__(self,name,description,date,priority):
            self.name=name
            self.description=description
            self.date=date
            self.priority=priority
            with open(task,'a') as f:
            f.write(name+" "+description+" "+date" "+priority)
        def list():
          with open(task,'r') as f:
            f.readlines()
