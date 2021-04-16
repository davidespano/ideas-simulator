# IDEAS simulator API
Repository for testing calls to the IDEAS simulator

## Installation
Clone or download the repository and run 

    pip install flask
    pip install flask-cors

for running the test you will be needing also pytest

    pip install pytest
    pip install pytest-flask

## Run
From the project directory run 

    python server.py

It will start a development server on your machine

## Methods
    http://127.0.0.1:5000/simulator
Receives an input object via post, validates it and returns 
a stub output if the validation is correct. If the validation 
fails, it returns a json object

```javascript
{
  'valid': true,
  'description': 'A string describing the error'
}
```

    http://127.0.0.1:5000/ 
Validates a test input object (provided by Pupin)

    http://127.0.0.1:5000/output
Validates an output object (provided by Pupin)

## Tests
We defined some client tests in the test_api.py file
You can run the tests using pytest on the project home. 

    pytest

