# aws-flashcards
AWS Lambda DynamoDB Flashcards API & Flask App
This project consists of two parts:

AWS Lambda function providing a REST API to fetch flashcard data from a DynamoDB table.

Flask web application that consumes the API and displays categorized flashcards.

AWS Lambda DynamoDB REST API
Features
Health check endpoint at /status

Retrieve all items from DynamoDB at /items

Handles conversion of DynamoDB Decimal types for JSON compatibility

Basic error handling

Setup
Configure AWS credentials

Update Lambda code with your AWS region and DynamoDB table name

Deploy Lambda and configure API Gateway with proxy integration

API Endpoints
Method	Path	Description
GET	/status	Service health check
GET	/items	Get all flashcard items

Flask Flashcards App
Overview
The Flask app fetches flashcards from the above API, organizes them by category, and serves them via several endpoints and a web UI.


Flask Routes
Route	Description
/	Renders HTML page with flashcards
/flashcards	Returns all flashcards as JSON
/categories	Returns list of all categories
/category/<category_name>	Returns flashcards for category
/flashcard/<flashcard_id>	Returns a single flashcard by ID

Running the Flask App
Set the API URL in the Flask app code (url = "YOUR URL HERE").

Install dependencies (flask, requests).

Run the app:

bash
Copy
Edit
python app.py
Open browser at http://localhost:5000.

Dependencies
Python 3.x

boto3 (for AWS Lambda)

Flask (for the web app)

requests (for API calls in Flask app)
