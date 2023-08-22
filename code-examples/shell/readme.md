
### Running the Shell Script

1.  **Open Terminal**: Open a terminal window on your computer.
    
2.  **Navigate to Directory**: Navigate to the directory containing the `post_request.sh` file using the `cd` command. For example:
    
    `cd /path/to/script/directory` 
    
3.  **Make Script Executable**: Make sure the script file has executable permissions. If not, use the following command to grant execution permission:

    `chmod +x post_request.sh` 
    
4.  **Run the Script**: Execute the shell script by entering the following command:
    
    `sh post_request.sh` 
    
5.  **Expected Outputs**: You should see one of the following responses from the server printed in the terminal.

**Successful**: Response: {"state":"success","id":"id-here"}

**Incorrect API key**: Response: {"state":"error","error":"permission denied"}

**Incorrectly formated XARF**: Response: {"state":"error","error":"validation failed"}