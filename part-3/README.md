##  Google Sign In with Your Flask URL Shortener
Copy your project from part-2 into the part-3 directory. Our goal is the modify the application such that a user may or may not be authenticated. Again, let's keep it simple and assume that anyone that is authenticated has every right to use all the application's features and someone who is not may only use some of the features.

Remember the application will have the following routes. You must use templates with the home and list routes. You can optionally use templates with the url and delete routes. The routes that are only accessible to authenticated users are labeled as authenticated-only.

* home - authenticated-only - This is the index page. Using `GET`, the webform for shortening a URL is presented. Using `POST`, a new ShortUrl object is created and stored. When a URL is successfully created and stored a message is given on the page and the web form is shown again. If a URL is not successfully created (duplicate or malformed), then an error message is shown and the web form is shown again.
* list - authenticated-only - List all shortened URLs as rows in an HTML table. The table shall have five columns. The first column is the ShortUrl id, the second is the ShortUrl original URL, the third is the ShortUrl short URL, the forth is the ShortUrl creation date, and the fifth is a hyperlink to delete/<id> where id is the ShortUrl object's id in the database.
* url/<short_code> - Given the short_code, look up the URL in the database and redirect the web browser to the original URL.
* delete/<id> - authenticated-only - Given the id, remove that object from the database. If successful, the list page reloads otherwise an error message is shown on the list page.

The author of Flask-Dance, David Baumgold, has written several demonstration projects for Google authentication with Flask-Dance. The project [flask-dance-google-security-sqla](https://github.com/singingwolfboy/flask-dance-google-security-sqla) demonstrates using Flask-Dance and Flask-Security with Google authentication.


