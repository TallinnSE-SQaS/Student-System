# Student-System
This repository contains the code for the Software Quality and Standards project.

Python is required to run it; you can download it from https://python.org/downloads or
from your distribution's package repository.

Take your time and read the _make_ scripts (for [Windows](make.cmd) and [Unix](make.sh))
so you can understand how to install dependencies, migrations, and run the development server.

For the sake of simplicity, virtual envs are not used. Instead, dependencies are installed into
a local directory, ".env", which is _git-ignored_. The _make_ script takes care of setting
the required environment variables in order to run the server correctly.

Also, make sure to install the Python (`ms-python.python`) and Pyright (`ms-pyright.pyright`) extensions
for VSCode for debugging, linting and artificial static typing using type annotations.
