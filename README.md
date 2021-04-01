# IDEAS simulator API
Repository for testing calls to the IDEAS simulator

## Installation
Clone or download the repository and run 

    pip install flusk

## Run
From the project directory run 

    python api.py

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
