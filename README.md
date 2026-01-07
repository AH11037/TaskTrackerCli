# Task Tracker
This is my second big project. It is a command-line task manager that lets you **add, update, delete and track tasks** </br>
Tasks are stored in a JSON file, each with their own unique ID, status and timestamps
## Features
<img height="1300" alt="image" src="https://github.com/user-attachments/assets/f7b16c22-2828-4e58-af1a-c025784d38ad" />

* Add tasks with their descriptions
* Update tasks descriptions or status (`todo`, `in-progress`, `done`)
* Delete tasks
* List tasks with optional filters:
  * All tasks
  * Only `todo`
  * Only `in-progress`
  * Only `done`
* Automatic task ID management with reusable IDs
* Tracks **createdAt** and **updatedAt** timestamps
* Persistent storage in `tasks.json`
* Fully CLI-based using `argparse`
## Installation & Running
* Download `task-cli.py`
* Open a terminal in the folder containing the file
* Run commands using: </br>
```python task-cli.py <command> [options]```
### Usage Examples
* Show help for the program </br>
```
python task-cli.py -h
```
* Show help for a specific command </br>
```
python task-cli.py add -h
python task-cli.py list -h
```
* Adding a new task </br>
```
python task-cli.py add "Feed the dogs"
```
* Mark a task in-progress </br>
```
python task-cli.py mark-in-progress 0
```
* Mark a task as done </br>
```
python task-cli.py mark-done 1
```
* Update a task description </br>
```
python task-cli.py update 2 "Practice Python for 1 hour"
```
* List all tasks </br>
```
python task-cli.py list
```
* List only todo tasks </br>
```
python task-cli.py list todo
```
* List only in-progress tasks </br>
```
python task-cli.py list in-progress
```
* List only done tasks </br>
```
python task-cli.py list done
```
* Delete a task </br>
```
python task-cli.py delete 1
```
## How It Works
* Tasks are stored individually in `tasks.json` as JSON objects
* Each task has:
  * `id` : unique numeric ID
  * `description` : the task text
  * `status` : `todo`, `in-progress` or `done`
  * `createdAt` : timestamp of creation
  * `updatedAt` : timestamp of last update
* Task IDs are automatically managed at `id.txt` . Deleted IDs are recycled
## What I Learned
* Using `argparse` to build CLI programs with subcommands
* Managing IDs and states persistently
## Future Improvements
* Adding priority levels for tasks
* Add due dates and reminders
* Add color for each of the respective statuses
* Add a search function
* Add a GUI using TKinter
