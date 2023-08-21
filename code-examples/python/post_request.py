import requests

# Set the URL you want to make the POST request to
url = 'https://datachannels.abusix.com/data/xarf'

# Set the API key
api_key = 'your-api-key'

# Set the data you want to send in the POST request
data={
  "Version": "3",
  "ReporterInfo": {
    "ReporterOrg": "ExampleOrg",
    "ReporterOrgDomain": "example.com",
    "ReporterOrgEmail": "reports@example.com",
    "ReporterContactEmail": "contact@example.com",
    "ReporterContactName": "Mr. Example",
    "ReporterContactPhone": "+ 01 000 1234567"
  },
  "Disclosure": True,
  "Report": {
    "ReportClass": "Activity",
    "ReportType": "Spam",
    "ReportSubType": "Trap",
    "Date": "2018-02-05T14:17:10Z",
    "SourceIp": "192.0.2.55",
    "SourcePort": 54321,
    "DestinationIp": "198.51.100.33",
    "DestinationPort": 25,
    "SmtpMailFromAddress": "spam@example.com",
    "SmtpRcptToAddress": "victim@example.com",
    "Samples": [
      {
        "ContentType": "message/rfc822",
        "Base64Encoded": True,
        "Description": "The spam mail",
        "Payload": "bWFpbA=="
      }
    ]
  }
}

# Set custom headers
headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

# Make the POST request using requests
response = requests.post(url, json=data, headers=headers)

# Print the response
print('Response:', response.text)