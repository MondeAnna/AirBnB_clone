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
