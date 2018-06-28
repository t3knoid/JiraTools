The FindTicketsWithoutMergedTo script searches Jira tickets based on a given JQL and returns the ones that have
no "Merged to" relationship."

This script assumes that you have Python installed. This should work with both version 2.7 and version 3.0 of Python. 

Make sure to install Virtualenv using the following command:

C:\Python27\python -m pip isntall virtualenv

Populate the Jira.jql file with the JQL that will result in Jira tickets that you want to examine.

Execute run.bat to execute the script.
