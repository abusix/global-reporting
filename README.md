# Global Reporting

Welcome to the Global Reporting Project! Abusix is revitalizing the Global Reporting Project, a free reporting service that aims to block network abuse. This project is designed to help with examples on how to submit XARF to our API endpoint. This repository contains simple examples in different programming languages demonstrating how to perform a POST request to our XARF API endpoint.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Running the Examples](#running-the-examples)
- [Contributing](#contributing)
- [License](#license)

## Description

This project showcases examples of performing a POST request using different programming languages. The examples are available in JavaScript, Python, and Shell Script.

## Getting Started

### Prerequisites

Follow this document to get your API key: https://docs.abusix.com/data-channels/5q9CV1FJbGR3vWZqVAYrqa/submitting-data-via-the-api-to-data-channels/aJPW14NYRRAQqsGDZnfA4w

Before running the examples, ensure you have the following prerequisites installed:

- Node.js and npm (for JavaScript)
- Python and pip (for Python)
- [cURL](https://curl.se/) (for Shell Script)

### Running the Examples

1.  **JavaScript**:

- Navigate to the `javascript` directory.
- Update your API key
- Install the required dependencies using `npm install`.
- Run the example script using `node post_request.js`.

2.  **Python**:

- Navigate to the `python` directory.
- Update your API key
- Install the required dependencies using `pip install requests`.
- Run the example script using `python post_request.py`.

3.  **Shell Script**:

- Navigate to the `sh shell` directory.
- Update your API key
- Make the shell script executable using `chmod +x post_request.sh`.
- Run the example script using `./post_request.sh`.

### Responses

**Successful**:
```  
status: 201 Created
{
	"state": "success",
	"id": "id-here"
} 
```

**Incorrect API key**: 
```  
status: 403 Forbidden
{
	"state": "error",
	"error": "permission denied"
}
```

**Incorrectly formated XARF**:

```  
status: 400 Bad Request
{
	"state": "error",
	"error": "validation failed"
}
```

## Contributing

Contributions are welcome! If you'd like to add more examples or improve existing ones, feel free to open a pull request.
