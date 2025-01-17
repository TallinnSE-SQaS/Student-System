@ECHO OFF
SETLOCAL ENABLEEXTENSIONS

:: This script is supposed to help setting up the environment necessary to
:: install dependencies and run the application.
::
:: Calling it without arguments will run `main`, which will install
:: dependencies, set the PYTHONPATH environment variable and, launch
:: Visual Studio Code (provided it is available in the PATH environment variable).
::
:: You can call this script with one of these arguments:
::
:: pip      -- installs dependencies into the .env directory. Necessary to specify what you want
::             pip to do. A single argument ARG will make it try to install the dependency called
::             ARG, if it exists. -r ARG will try to install the dependencies specified in the file
::             ARG - usually requirements.txt.
:: code     -- launches VSCode with the required PYTHONPATH env var.
:: server   -- runs a development server on port 5000 (can be accessed on http://localhost:5000)
:: test     -- runs automated tests
:: migrate  -- runs the migrations in the migrations directory (to be implemented).
::             (not yet implemented)

GOTO :main

:pip
python -m pip install -t .env %*
GOTO :EOF

:code
SET PYTHONPATH=.env
START /B code .
GOTO :EOF

:server
SET PYTHONPATH=.env
START python main.py devserver
GOTO :EOF

:test
SET PYTHONPATH=.env
SET ENV=test

python -m unittest discover -v tests/
GOTO :EOF

:migrate
SET PYTHONPATH=.env
python main.py migrate
GOTO :EOF

:main
IF "%~1" NEQ "" (
    CALL :%*
) ELSE (
    CALL :pip -r requirements.txt
    CALL :code
    CALL :server
)
