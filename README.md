
# bottle_parse_palindrome
A simple API with bottle to parse palindromes

# Overview:

The app has 3 API end points:
/palindrome<input> which takes a string as input, checks if it is a palindrome and adds it to a sqllite database
/palindromes which takes a new-line separated text file of words and sentences as input, checks if the lines / words are palindromes and returns a true | false per line as the API resposne
/palindromes/history which returns all the palindromes sent in through the palindrome<input> endpoint

## To run the app:
* create a pipenv shell run ```pipenv install```
* run ```python app.py``` and the app will run on the local server
* to use the first and third api end points (both GET requests) make the request from the browser
* to use the file upload end point you will need either Thunder Client or Postman - please send the file as Form \ Form Data (files) and the input variable for the file is "upload_file"
