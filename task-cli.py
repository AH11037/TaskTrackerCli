
import json
import os
import argparse
import datetime

ID_File = "id.txt"
Task_File = "tasks.json"

#Make JSON file
if not os.path.exists(Task_File):
    with open(Task_File, 'w') as file:
        json.dump([], file)

if not os.path.exists(ID_File):
    with open(ID_File, 'w') as file:
        TaskNo = 0
        file.write(f"{TaskNo}\n")


with open(ID_File, 'r') as idFile:
    lines = idFile.readlines()
    TaskNo = int(lines[0].strip())
    available_ids = set(map(int, lines[1].strip().split(','))) if len(lines) > 1 else set()

if os.path.getsize(Task_File) == 0:
    with open(Task_File, 'w') as file:
        json.dump([], file)
        Tasks = json.load(file)
else:
    with open(Task_File, 'r') as please:    
        Tasks = json.load(please)

#Useful functions
def save_id_data(available_ids):
    with open(ID_File, 'w') as file:
        file.write(f"{TaskNo}\n")
        file.write(','.join(map(str, available_ids)))

def sorttasks(tasks):
    return sorted(tasks, key = lambda x:x['id'])

def add(content):
    current_time = datetime.datetime.now()
    global TaskNo, available_ids
    with open(ID_File, 'r') as x:
        lines = x.readlines()
        TaskNo = int(lines[0].strip())
    if available_ids:
        id_to_use = min(available_ids)
        available_ids.remove(id_to_use)
    else:
        id_to_use = TaskNo
        TaskNo += 1
    d = {}
    d['id'] = id_to_use
    d['description'] = content
    d['status'] = "todo"
    d['createdAt'] = (f"{current_time.hour}:{current_time.minute} {current_time.day}/{current_time.month}/{current_time.year}")
    d['updatedAt'] = None
    id =d["id"]
    Tasks.append(d)
    with open(Task_File, 'w') as file:
        json.dump(Tasks, file, indent = 5)
        print(f"Task added successfully (ID:{id})")
        save_id_data(available_ids)

def readall(filter = "none"):
    with open(Task_File, 'r') as file:
        reading = json.load(file)
        x = sorttasks(reading)
        filteredlist = []
        if filter == "done":
            for task in x:
                if task["status"] == "done":
                    filteredlist.append(task)
        elif filter == "todo":
            for task in x:
                if task["status"] == "todo":
                    filteredlist.append(task)
        elif filter == "in-progress":
            for task in x:
                if task["status"] == "in-progress":
                    filteredlist.append(task)
        else:
            filteredlist = x
        print("\nCurrent Tasks:")
        print("=" * 40)  # Print a separator line
        for task in filteredlist:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created At: {task['createdAt']}")
            print(f"Updated At: {task['updatedAt'] if task['updatedAt'] else 'Not updated'}")
            print("-" * 40)
        if filter == "none":
            with open(Task_File, 'w') as file:
                json.dump(x, file, indent = 5)

def delete(deletion):
    global TaskNo
    deletelist = []
    with open(Task_File , 'r') as file:
        deletefile = json.load(file)
        for x in deletefile:
            if x['id'] != deletion:    
                deletelist.append(x)
    with open(Task_File, 'w') as wFile:
        json.dump(deletelist, wFile, indent = 5)
        print(f"Task deleted successfully ID:{deletion}")
    available_ids.add(deletion)
    save_id_data(available_ids)

def update(i, k ,v):
    current_time = datetime.datetime.now()
    Tasks[i][k] = v
    Tasks[i]["updatedAt"] = (f"{current_time.hour}:{current_time.minute} {current_time.day}/{current_time.month}/{current_time.year}")
    with open(Task_File, 'w') as file:
        json.dump(Tasks, file, indent = 5)
        print("Task updated successfully")

#Arguments
parser = argparse.ArgumentParser(description = "Task Manager")
subparsers = parser.add_subparsers(dest = "command")

#Commands
#Delete
delete_parser = subparsers.add_parser("delete", help = "Delete a task")
delete_parser.add_argument("id", type = int)

#Add
add_parser = subparsers.add_parser("add", help = "Add a new task")
add_parser.add_argument("addTask", type = str)

#Update
update_parser = subparsers.add_parser("update", help = "Update a given task")
update_parser.add_argument("id", type = int)
update_parser.add_argument("updateTask", type = str)

#Mark-in-progress
progress_parser = subparsers.add_parser("mark-in-progress", help = "Marks a given task 'in-progress'")
progress_parser.add_argument("id", type = int)

#Mark-done
MarkDone_parser = subparsers.add_parser("mark-done", help = "Marks a given task as done")
MarkDone_parser.add_argument("id", type = int)

#List
list_parser = subparsers.add_parser("list", help = "Lists all tasks")
list_subparsers = list_parser.add_subparsers(dest = "list_command")
done_parser = list_subparsers.add_parser("done", help = "Specifies to list only the done tasks")
todo_parser = list_subparsers.add_parser("todo", help = "Specifies to list only the todo tasks")
in_progress_parser = list_subparsers.add_parser("in-progress", help = "Specifies to list only the in-progress tasks ")

args = parser.parse_args()
#The big if
if args.command:
    if args.command == "add":
        add(args.addTask)
    elif args.command == "delete":
        delete(args.id)
    elif args.command == "update":
        update(args.id, "description", args.updateTask)
    elif args.command == "mark-in-progress":
        update(args.id, "status", "in-progress")
    elif args.command == "mark-done":
        update(args.id, "status", "done")
    elif args.command == "list":
        if args.list_command == "done":
            readall(filter = "done")
        elif args.list_command == "todo":
            readall(filter = "todo")
        elif args.list_command == "in-progress":
            readall(filter = "in-progress")
        else:
            readall()