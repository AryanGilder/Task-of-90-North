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


2.  
Here are step-by-step solutions for the requested AWS Lambda functions:

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
python
Copy
Edit
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
json
Copy
Edit
{
    "num1": 5,
    "num2": 7
}
Run the test and verify the result:
json
Copy
Edit
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
