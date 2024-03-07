### AirBnB clone

A simple, deployable clone of the AirBnB website.

<br />

#### Final Product: Front-End

[Landing Page](img/fin-prod.png)

<br />

#### Final Product: Back-End

When run in `interactive` mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

<br />

When run in `non-interactive` mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<br />

#### Objectives

A website capable of the following functionality:
    * A user friendly website
    * A RestfulAPI
    * Data manipulation via a `cli`
    * Data storage

<br />

#### Project Portions: The Command Line Interface

This provides the developer an interface allowing for the `creation`, `reading`, `updating` and `deletion` of data.

<br />

#### Storage

The driving ideology is that the developer is to have ease of use by separating data management from its technical execution. What this then allows is for the data to be managed both from the `cli` as well as any other interface (e.g. `GUI`), all to the same effect.

This abstraction also allows for the storage format to be changed without effect to the code. This in turn means that should the manner in which one wishes to make the data persist becomes a matter of providing the 'plugin' that stores in said format.

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * How to create a Python package
    * How to create a command interpreter in Python using the `cmd` module
    * What is Unit testing and how to implement it in a large project
    * How to serialize and deserialize a Class
    * How to write and read a JSON file
    * How to manage `datetime`
    * What is an `UUID`
    * What is `*args` and how to use it
    * What is `**kwargs` and how to use it
    * How to handle named arguments in a function

<br />

#### Requirements: General

* Allowed editors:
    * `vi`, `vim` or `emacs`

* A `README.md` file, at the root of the folder of the project, is mandatory

* Expected of all files:
    * Interpretable/compileable on `Ubuntu 20.04 LTS` using `python3` (version `3.8.5`)
    * End with a new line
    * As the first line, have `#!/usr/bin/python3`
    * To be linted using `pycodestyle` (version `2.8.*`)
    * Be executable
    * Be documentated, examples
        * Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
        * Functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
        * Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
        * Methods: `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

<br />

#### Requirements: Python Unit Tests

* Expected of all tests:
    * To be inside the folder `tests`
    * To use the `unittest` module
    * Be python files

* File organisation:
    * All test files and folders should start by `test_`
    * `tests` folder organisation tobe the same as with the scripts being tested, e.g.:
        * Script: `models/base_model.py`  --  Unit Tests: `tests/test_models/test_base_model.py`
        * Script: `models/user.py`  --  Unit Tests: `tests/test_models/test_user.py`

* Test execution should be achievable in the following manners:
    * Using this command: `python3 -m unittest discover tests`
    * You can also test file by file by using this command
    * Executing a file with this command: `python3 -m unittest <path to file>`
        * e.g: `python3 -m unittest tests/test_models/test_base_model.py`
    * As run in non-interactive mode: `echo "python3 -m unittest discover tests" | bash`

<br />
