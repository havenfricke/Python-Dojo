import subprocess                       # import built-in CLI tool

class RHELAutomator:        
    def __init__(self):
        pass                            # Create class and "pass" property construction


    def run_command(self, cmd_list):    # Executes command in CLI and returns output
        try:                            # trycatch block or tryexcept in python

            res = subprocess.run(       # store the result (res) of subprocess.run()
                cmd_list,               # subprocess.run() is a built in method tthat executes 
                capture_output=True,    # and manage external commands or programs from within a Python script. 
                text=True,              # It is a synchronous function that waits for the command to complete 
                check=True              # and returns a CompletedProcess instance, which contains the results of the execution.
            )

            return res.stdout.strip()  # return the response from standard output (capture_output=True argument enables this)
        
        except subprocess.CalledProcessError as e:  # a Python exception raised when a command executed via the subprocess 
                                                    # module returns a non-zero exit code, indicating that the command failed.
            self.log_error(e)                       # reference self or this class and called log_error(), pass the aliased exception

            return None                             # complete the process by returning null or nothing
            
    def log_error(self, e):                         # error log utility called within the except block of tryexcept
        print(f"Command '{' '.join(e.cmd)} failed with: {e.stderr}\n")


bot = RHELAutomator()                   # Store an instance of the class here as "bot"






