py-1337
==============

Yet another py code repo
--------------

Clone repo
```
    $ git clone https://github.com/mayukh42/py-1337.git
```


Run tests
--------------

In the root dir of repo, create a virtualenv, add current project root to PYTHONPATH, then run the tests
``` 
    $ python -m venv .venv
    $ export PYTHONPATH="$(pwd):$PYTHONPATH"
    $ python tests/item.py
```

Alternately, run setup.sh to automate the above:
```
    $ . ./setup.sh
```

TBA
