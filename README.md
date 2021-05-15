# FastAPI_apis

Math Module:

``` 
../math1/{nterm} - calculates and returns n th Fibonacci passes as endpoint (n &gt; 1 &lt; 100) with time complexity of worse: O(N) best:
O(1)
../math2/{input_number} - calculates and return the factorial of a n number passed as an endpoint with time complexity of O(n)

```


String Module

```
../string1/{word} - calculates and returns the length of input string passes as endpoint string
../string2/{input_length}/{input_word} - generate and return a string of a given length of a chosen character as input, length of character and character string is passed as an input.
```


#Steps to run the API

1) Firstly, ensure you have Python3 installed on your system and then in CMD - ```pip install -r requirements.txt```
2) Start the server with ```uvicorn main:app --reload```
