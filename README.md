# Task Manager CLI Application

# Overview

This is a command-line interface (CLI) application for managing tasks.
Users can add, view, delete, mark tasks as completed and Exit.
The application also includes a simple login with mailid and logic system with dummy credentials.

# Features

 1. Login System : A basic login system that requires a valid email and password.I had given dummy email and password.
 2. Email : demo@gmail.com
 3. password : Taskmanager@Demo
 4. Add a Task : Users can add new tasks to the task list.
 5. View Tasks : Users can view all tasks along with their completion status - completed or not completed.
 6. Delete a Task : Users can delete a task by its ID.
 7. Mark Task as Complete : Users can mark a task as completed.
 8. And finally exit
 9. Task Manager CLI Application
  Enter the Email: demo@gmail.com
  Enter the Password: Taskmanager@Demo
  Login successful ✅
  Task Manager
  1. Add a task ➕
  2. View tasks 📋
  3. Delete a task 🗑️
  4. Mark task as complete ✅
  5. Exit ➡️
  Enter your choice: 2
  Task 1: interview preparation  [ Completed ✅ ]
  Task 2: update resume  [ Not Completed❌ ]
  Task 3: projects [ Not Completed❌ ]

  Task Manager
  1. Add a task ➕
  2. View tasks 📋
  3. Delete a task 🗑️
  4. Mark task as complete ✅
  5. Exit ➡️
  Enter your choice:

    

# Technologies Used

1. Python
2. JSON for data storage
3. OS for file handling
   
## How to Run the Application

1. Ensure you have Python installed on your machine.
2. Clone the repository:
   git clone <repository_url>
   git clone https://github.com/Swethuvenkatesan/Task-Manager-CLI-Application.git
3. Navigate to the project directory:
cd Task-Manager-CLI-Application
4. Run the application:
python task_manager.py

## Code Explanation
1.Imports

import json
import os
json: Used for reading and writing tasks to a JSON file.
os: Used for checking the existence of the tasks file.
