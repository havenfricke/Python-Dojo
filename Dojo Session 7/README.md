### CLI WITH PYTHON VIRTUAL ENVIRONMENTS, HTTP REQUESTS, AND PACKAGE INSTALLATION

- This dojo session comes with no files. You'll be making everything from the ground up with these instructions.

### SOME PREFACE
- Python packages are primarily installed using pip, the standard package manager for Python.
- The most common and recommended approach is to use a virtual environment for each project to manage dependencies separately.
- A dependency is a library of code or packaged code available for use in a development environment.
- A Python virtual environment is best practice across operating systems to avoid core OS conflicts and isolate project-specific libraries.
- To open a folder in VS Code with the CLI, use the command cd to move down to the folder/directory, then use `code .` using CLI
- The command `cd ..` will move up in the directory structure.
- To create a folder using the CLI, use `mkdir folder_name`.
- To create a file using the CLI, use `touch file_name.py`.
- PRO TIP: Typically you can use `cd folder_name` if there are no spaces in the folder name, but if there are, wrap the folder name in quotes.
- EXAMPLE: `cd "Dojo Session 7"`


### VIRTUAL ENVIRONMENT (ACTIVATION AND DEACTIVATION)
- In VS Code, you can access the terminal using the shortcut ctrl + ` (backtick/tilde key).
- `cd` into `"Dojo Session 7"`
- Create the Python virtual environment: `python -m venv env_name`
- Activate the environment: `cd env_name` into the virtual environment created, then `source bin/activate` (Linux) or `.\Scripts\Activate.ps1` (Windows PowerShell).
- `cd ..` out of the environment folder after it is activated (you should see your (env_name) to the left of your CLI/terminal text).
- If you get errors, `cd ..` out of the environment folder, delete the environment folder that was created then try again.
- To deactivate the virtual environment and go back to normal CLI usage: type `deactivate`.


### PACKAGE INSTALLATION AND FILE CREATION
- For the purpose of this dojo session, we are going to install Python requests and flask, create some files, then switch python interpreters.
- Python requests is an open-source library to make requests over the HTTP protocol (client side).
- Python flask is an open-source web server library for sending data over the HTTP protocol (server side).
- These allow you to reach web servers that are hosted over the internet, and create your own web server APIs.
- The standard HTTP methods are GET, POST, PUT, and DELETE.
- These are for reading, writing, editing, and deleting data in that respective order.
- For more info and documentation on Python requests -> https://pypi.org/project/requests/
- For more info and documentation on Python flask -> https://flask.palletsprojects.com/en/stable/
- To install requests, make sure your environment is activated in the CLI (terminal), then use `pip install requests`.
- To install flask, make sure your environment is activated in the CLI (terminal), then use `pip install flask`.
- This will install the packages in the "Lib" folder that was auto-installed when the Python virtual environment was created.
- Now in the root of your "Dojo Session 7" folder, use CLI commands `touch app_api.py` and `touch app.py`.
- There should now be a files named app_api.py and app.py in the root of your "Dojo Session 7" folder and an auto-generated virtual environment folder alongside these. 


### PYTHON INTERPRETERS
!!!IMPORTANT!!!
- When you drop the code found below this section into your files (app.py and app_api.py), you're going to get an import error
- To fix "Import could not be resolved" errors, press Ctrl + Shift + P in VS Code, type "Python: Select Interpreter", select it, then select "Enter interpreter path...", then select the interpreter located inside your virtual environment (Located in \Scripts\python.exe)
- This will switch from the Global Python Interpreter being used to recognize Python while it is being written in VS Code to the virtual environment specific interpreter.
- This will break the other files outside of your virtual environment (that is okay for now).
- To switch back, press Ctrl + Shift + P again and select Python X.XX.X (your global version). There should be text that says "Global" to the right. Select that one.
- For future projects using a virtual environment specific Python interpreter is crucial to avoid OS conflicts
!!!IMPORTANT!!!

- To use these scripts you need to have your virtual environment interpreter selected in VS Code, otherwise you'll get import errors




- This is for app_api.py using flask

```Python

from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple data store
items = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Mouse", "price": 25}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(port=5000)

```



- This is for app.py using requests

```Python

import requests

BASE_URL = "http://127.0.0.1:5000/api/items"

def test_get_items():
    response = requests.get(BASE_URL)
    print(f"GET Status: {response.status_code}")
    print(f"Data: {response.json()}")

def test_post_item():
    new_data = {"id": 3, "name": "Keyboard", "price": 50}
    response = requests.post(BASE_URL, json=new_data)
    print(f"POST Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_get_items()
    test_post_item()

```

- You are going to need two terminals to run these scripts
- What we are doing here is simulating a basic client and server
- With your virtual environment activated `cd` into "Dojo Session 7"
- Use command `python app_api.py`
- You should see a message in the terminal that looks similar to:

```Powershell

 * Serving Flask app 'app_api'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [20/Mar/2026 14:42:02] "GET /api/items HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2026 14:42:02] "POST /api/items HTTP/1.1" 201 -

```

- The server/api is now live in development mode

- Next, open a new terminal by pressing the plus button in VS code located in the top right hand corner of the terminal window
- Activate you environment in the new terminal window then navigate to "Dojo Session 7" folder
- Run command `python app.py`
- You should see a message in the terminal that looks similar to:

```Powershell

GET Status: 200
Data: [{'id': 1, 'name': 'Laptop', 'price': 999}, {'id': 2, 'name': 'Mouse', 'price': 25}]
POST Status: 201
Response: {'id': 3, 'name': 'Keyboard', 'price': 50}

```

- If you see both of these messages in each terminal, you've successfully requested and served data over HTTP in a development environment