# Django Chat Application

This is a Django-based chat application that allows users to sign up, log in, and chat with others. This project utilizes WebSockets for real-time messaging.

## Setup Instructions

1. **Clone the Repository**:
    Clone the project from GitHub:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    
2. **Install Dependencies**:
    Navigate to the project directory and install the required dependencies:
    ```bash
    cd your-repository
    pip install -r requirements.txt
    
3. **Configure the Database**:
    Run migrations to set up the database:
    ```bash
    python manage.py migrate
    
4. **Collect Static Files** (For production):
    If you're deploying to production, make sure to collect static files:
    ```bash
    python manage.py collectstatic
    
5. **Run the Project Locally**:
    Start the Django development server to run the project locally:
    ```bash
    python manage.py runserver

6. **Open the Application**:
    Open your browser and navigate to `http://127.0.0.1:8000/` to access the chat application.

#Common Issues and Troubleshooting Steps

Currently, I am encountering a 500 Internal Server Error when deploying the application. Despite my efforts to troubleshoot and resolve the issue, 
I was unable to fix it within the given timeframe. I am actively working on identifying and addressing the root cause, and with more time or guidance, 
I am confident I can resolve this issue promptly. Thank you for your understanding.

#AWS Task : 

1. AWS Lambda Function to Add Two Numbers
Steps:
Login to AWS Console:

Go to the AWS Management Console.
Navigate to the Lambda service.
Create a Lambda Function:

Click on Create Function.
Choose Author from Scratch.
Provide a name (e.g., AddTwoNumbersFunction).
Choose a runtime (e.g., Python 3.9).
Click Create Function.

Write the Function Code:

In the Code tab, replace the default code with the following Python function:

def lambda_handler(event, context):
    # Get the numbers from the event payload
    num1 = event.get("num1", 0)
    num2 = event.get("num2", 0)

    # Calculate the sum
    result = num1 + num2

    return {
        'statusCode': 200,
        'body': {
            'num1': num1,
            'num2': num2,
            'result': result
        }
    }
Test the Function:

Click Test and configure a new test event.

Add the following JSON to the test event:

{
    "num1": 5,
    "num2": 7
}

Run the test and verify the result:

{
    "statusCode": 200,
    "body": {
        "num1": 5,
        "num2": 7,
        "result": 12
    }
}


2. AWS Lambda Function to Store a Document or PDF in an S3 Bucket

Prerequisites:

Ensure an S3 bucket exists (e.g., my-documents-bucket).

Attach an IAM role to the Lambda function with the AmazonS3FullAccess policy.

Steps:

Create a Lambda Function:

Navigate to the Lambda service.
Create a new function (e.g., UploadPDFToS3).
Choose Python 3.9 as the runtime.

Write the Function Code:

import boto3
import base64

def lambda_handler(event, context):
    # S3 bucket name
    bucket_name = "my-documents-bucket"

    # File name and content from event
    file_name = event.get("file_name", "default.pdf")
    file_content_base64 = event.get("file_content", "")
    
    # Decode the Base64 file content
    file_content = base64.b64decode(file_content_base64)

    # Initialize the S3 client
    s3 = boto3.client('s3')

    try:
        # Upload file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded successfully to bucket {bucket_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error uploading file: {str(e)}'
        }
Set Up the S3 Bucket:

Ensure the S3 bucket (my-documents-bucket) exists.
Update the bucket permissions to allow your Lambda function's IAM role to upload files.
Test the Function:

Prepare a sample PDF file, encode it in Base64, and create a test event:

{
    "file_name": "test-document.pdf",
    "file_content": "BASE64_ENCODED_CONTENT_HERE"
}

To get the Base64 encoded content:
Use a tool or Python script:

import base64
with open("path/to/your/document.pdf", "rb") as pdf_file:
    print(base64.b64encode(pdf_file.read()).decode('utf-8'))

Run the test. Check the S3 bucket for the uploaded file.

Verify in S3:

Navigate to your S3 bucket and verify the file is uploaded successfully

