@echo off
python -m virtualenv env
call env\Scripts\activate
python -m pip install --trusted-host pypi.python.org -r requirements.txt
cls
python FindTicketsWithoutMergedTo.py
echo.
deactivate
