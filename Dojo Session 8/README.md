### SUBPROCESS (PYTHON LIBRARY), AND CLI AUTOMATION

**The CLI commands in this dojo are not for windows. Consider switching to linux (RHEL) to participate.**

### SUBPROCESS
- This is a built-in python library specifically for running CLI commands from a python program
- The run() method is primarily responsible for executing commands


### CLI AUTOMATION
- By using the run method found in the subprocess python library, we can send commands by list
- run() has over 20 parameters however there are only several that apply to CLI automation
- In this dojo we'll be passing an array as an argument to run() as 'cmd_list' or command list
- Crucial arguments to automate CLI commands include capture_output, text, and check
- capture_output is a bool, telling subprocess to return a string output of CLI commands
- text is a bool and specifies that the outputs should be handled as strings
- check is a bool that tells run() to raise an error if the command fails


*This dojo is broken up into two files to exercise clean architecture. Additional refactoring would be useful within run.py.*
*The logic within run.py could be moved into a separate file and placed into a method or function then, called within run.py*


