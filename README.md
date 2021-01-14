# CPSC 223p
# Lab 08
Web applications is where the action is at (and machine learning). Let's learn a little about making a web application using Python.

## Objectives
* Get introduced with Flask
* Make a hello world web application
* Use Google sign in

## Flask
We shall be using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and a number of other Python packages. Remember that we use Python's virtual environments to configure each project.

Secondly, Flask has great online documentation and the CSUF library has an excellent full-text book available online. The book [Flask Web Development](https://csuf-primo.hosted.exlibrisgroup.com/permalink/f/43rjjt/TN_cdi_askewsholts_vlebooks_9781491991718) book by [Miguel Grinberg](https://blog.miguelgrinberg.com/) is available through the [CSUF library](http://www.library.fullerton.edu/).

Lastly, Miguel Grinberg has [the Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for those uninterested in books.

# Instructions
Write a program for each exercise sub-directory. Each exercise subdirectory is prefixed with the string `part-`.

Every file that you submit must have a header. On the file that contains the main function, start the file with `#!/usr/bin/env python3`. Change the comment line (the one starting with ```#```) to state your full name. On the next line, start a new comment and state which section of CPSC 223p you are enrolled in. On the next line, start a new comment and state today's date. On the next line, start a new comment and state your CSUF email address. On the next line, start a docstring and provide a short description of the program you are writing. For example, if your name is Tuffy Titan and you are in CPSC 223p-01, the comment may look something like
  ```
  #!/usr/bin/env python3
  #
  # Tuffy Titan
  # CPSC 223p-01
  # 2050-01-01
  # tuffy.titan@csu.fullerton.edu
  #
  """
  This my first program and it prints out Hello World!
  """
  ```

Please adhere to the [Google Python coding style](https://google.github.io/styleguide/pyguide.html). Please read the style guide and ensure your code conforms. If it does not, then your assignment may not receive full credit. You may use a linter, such as `pylint`, and a style checker, such as `pycodestyle`, to check your source code to verify that it conforms to the specified style.

# Rubric
Each exercise is worth 5 points. There is a total of 15 points possible. Your program must compile, in other words be syntactically correct, before it is graded. Submissions that do not compile shall be assigned a zero grade. 

For each problem:

* Functionality (3 points): Your submission shall be assessed for the appropriate constructs and strategies to address the exercise.

* Compilation (1 point): Your submission shall compile with no warnings. Compile with errors results in a zero grade.

* Readability (1 point): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is.
