## FastAPI Customer Management API
This is a simple API built with FastAPI for managing customer data. It provides endpoints for creating, retrieving, updating, and deleting customer records.

# Usage
Once the API is running, you can access the endpoints using the following URLs:

GET: http://127.0.0.1:8000/

Returns a welcome message indicating a successful GET request.
GET: http://127.0.0.1:8000/customer/{id}

Retrieves the customer record with the specified id. Replace {id} with the actual customer ID.
POST: http://127.0.0.1:8000/customer/

Creates a new customer record. Send a JSON payload with the following fields: first_name, last_name, email, and gender.
PUT: http://127.0.0.1:8000/customer/

Updates an existing customer record. Send a JSON payload with the updated fields: first_name, last_name, email, and gender.
PATCH: http://127.0.0.1:8000/customer/

Partially updates an existing customer record. Send a JSON payload with the fields to be updated: first_name, last_name, email, and gender.
DELETE: http://127.0.0.1:8000/customer/{id}

Deletes the customer record with the specified id. Replace {id} with the actual customer ID.
