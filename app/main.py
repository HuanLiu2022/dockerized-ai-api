# Import the FastAPI class so we can create a FastAPI application.
from fastapi import FastAPI

# Create a FastAPI application instance.
# This "app" object will contain our API endpoints.
app = FastAPI()


# Define a GET endpoint for the root path "/".
# When a client sends a GET request to "/", FastAPI calls the root() function.
@app.get("/")
def root():
    # Return a JSON response to the client.
    return {"message": "Hello, AI Engineer!"}


# Define a GET endpoint for "/analyze".
# The "text" parameter will be provided by the client as a query parameter.
@app.get("/analyze")
def analyze(text: str):
    # Count the number of characters in the input text.
    length = len(text)

    # Split the text into words and count them.
    words = len(text.split())

    # Return the analysis as JSON.
    return {
        "text": text,
        "length": length,
        "words": words
    }
