# CPSC 223p
##  Flask URL Shortener

Remember the book [Flask Web Development](https://csuf-primo.hosted.exlibrisgroup.com/permalink/f/43rjjt/TN_cdi_askewsholts_vlebooks_9781491991718) book by [Miguel Grinberg](https://blog.miguelgrinberg.com/) is available through the [CSUF library](http://www.library.fullerton.edu/). Miguel Grinberg has also written [the Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for those unwilling to use books.

Write a web application using the Flask framework which shortens URLs similar to how online services like bit.ly and tinyurl.com work. Your application will have a web form which someone can submit a url such as http://www.fullerton.edu/ and a new ShortUrl object shall be created which stores the original URL, the short url, and the date the object was created. The ShortUrl object is mapped to a relational database table such that the application can quickly recall any previously shortened URL.

The ShortUrl object has the following data members:
  
  * id an Integer and primary key
  * original_url The original URL that is not short
  * short_url The shortened URL from the original_url
  * created The date and time the object was created

The application will have the following routes. You must use templates with the home and list routes. You can optionally use templates with the url and delete routes.

* home - This is the index page. Using `GET`, the webform for shortening a URL is presented. Using `POST`, a new ShortUrl object is created and stored. When a URL is successfully created and stored a message is given on the page and the web form is shown again. If a URL is not successfully created (duplicate or malformed), then an error message is shown and the web form is shown again.
* list - List all shortened URLs as rows in an HTML table. The table shall have five columns. The first column is the ShortUrl id, the second is the ShortUrl original URL, the third is the ShortUrl short URL, the forth is the ShortUrl creation date, and the fifth is a hyperlink to delete/<id> where id is the ShortUrl object's id in the database.
* url/<short_code> - Given the short_code, look up the URL in the database and redirect the web browser to the original URL.
* delete/<id> - Given the id, remove that object from the database. If successful, the list page reloads otherwise an error message is shown on the list page.

Given a URL, for example https://www.fullerton.edu/, the URL will be mapped to a string which represents the URL. The string must be unique and the function used to map the URL to the string must be [bijective](https://en.wikipedia.org/wiki/Bijection). A bijection is a function which is invertible thus given the short string code, we can map that code back to the original URL.

(Although you should all be able to do the math, this isn't a serious computer science course so let I'll explain the algorithm and you implement it. And let's keep it simple - I'll leave it to the reader to worry about how this algorithm can be compromised and our implementation is susceptible to Javascript injection attacks.)

Let's call our shortening function urlshortcode() and our URL lookup function shall be called orignalurl().

Every ShortUrl object has a unique integer ID data member. Let's use the ID as the parameter to urlshortcode(). For example, if I want to shorten the ShortUrl with ID 1 then urlshortcode(1) is called. This returns a string which represents 1.

To map the integer given to urlshortcode() to a string, we shall convert the number to base 62. We shall use base 62 because there are 26 lower case letters in the alphabet (a-z), 26 capital letters in the alphabet (A-Z), and 10 digits (0-9) which totals to 62. In our base 62 counting system base 62 'a' is 0, base 62 'z' is 25, base 62 'A' is 26, base 62 'Z' is 51, base 62 '0' is 52, and base 62 9 is 61. If I wanted to represent the base 10 number 62 it would be `ba`. Here are a few other examples:

* base 10 100 is base 62 bM
* base 10 1000 is base 62 qi
* base 10 1654 is base 62 AQ

Note that the most significant digit is on the left in all the examples. Please follow the pattern given.

(Please do not waste your time trying to 'find' this code online. Just write it yourself.)

The inverse function, orignalurl(), shall take a string which is a base 62 number and map that number back to base 10. The base 10 number is the ShortUrl object's ID in the database.

The repository has a different layout from part-1. The application is in the directory named urlshortener. The application is defined as a Python module with an __init__.py file. The database creation is handled in cli.py. The database objects (the model) is defined in models.py, and the applications configuration is given in config.py. The application's URL routing should be defined in __init__.py or in a separate file named controller.py. The application's templates are in urlshortener/templates.

The project uses python-dotenv. There is a file named .env which defines the environment variables for this project.

 

