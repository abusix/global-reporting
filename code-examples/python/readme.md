### Running the Python Script

1.  **Install Python**: Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
    
2.  **Install requests Library**: Open a terminal and navigate to the directory containing the `post_request.py` file. Run the following command to install the required `requests` library:
    
    `pip install requests` 
    
3.  **Run the Script**: Once `requests` is installed, you can run the script using the following command:
    
    `python post_request.py` 
    
4.  **Expected Outputs**: You should see one of the following responses from the server printed in the terminal.

**Successful**: Response: {"state":"success","id":"id-here"}

**Incorrect API key**: Response: {"state":"error","error":"permission denied"}

**Incorrectly formated XARF**: Response: {"state":"error","error":"validation failed"}