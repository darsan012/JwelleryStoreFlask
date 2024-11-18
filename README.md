# Flask Application with MongoDB Integration and Automated Tests

This is a Flask application that connects to MongoDB and provides routes for interacting with the database. This project includes unit tests for Flask routes and MongoDB operations, with a CI/CD pipeline integrated via GitHub Actions.

## Features
- **Flask Routes**:
  - A home route (`/home`) that returns an HTML page.
  - A products route (`/products`) that fetches and displays products from a MongoDB database.
  
- **MongoDB Integration**:
  - Read operation: Fetching products from MongoDB.
  - Write operation: Inserting new products into MongoDB.

- **Automated Testing**: 
  - Unit tests for route responses and MongoDB operations.
  - Tests are run automatically in the CI pipeline on GitHub Actions.

## Prerequisites

To run the application and tests locally, you will need the following:

- Python 3.9 or higher
- Flask
- MongoDB (MongoDB Atlas or local setup)
- `pip` (Python package manager)
- GitHub account for CI/CD (GitHub Actions)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Set up a Virtual Environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate
```
### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```
### 4. Set up .env
```bash
MONGODB_USERNAME=your_username
MONGODB_PASSWORD=your_password
```
### 5.  Running the Application
```bash
python app.py
```
   Hurray! your app is running on http://127.0.0.1:5001/

### 6. Testing the application
```bash
python app/tests/__init__.py 
```