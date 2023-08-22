
### Running the JavaScript Script

1.  **Install Dependencies**: Before running the script, make sure you have Node.js and npm installed. If not, you can download and install them from [here](https://nodejs.org/).
    
2.  **Install axios**: Open a terminal and navigate to the directory containing the `post_request.js` file. Run the following command to install the required `axios` module:
    
    `npm install axios` 
    
3.  **Run the Script**: Once `axios` is installed, you can run the script using the following command:
    
    `node post_request.js` 
    
4.  **Expected Outputs**: You should see one of the following responses from the server printed in the terminal.

**Successful**: Response: { state: 'success', id: 'id-here' }

**Incorrect API key**: Error: { status: 403, state: 'error', error: 'permission denied' }

**Incorrectly formated XARF**: Error: { status: 400, state: 'error', error: 'validation failed' }