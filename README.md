# JiraTools
Misc Scripts used in managing Jira issues. This script assumes that you have Python installed. This should work with both version 2.7 and version 3.0 of Python. 

# Requirements
Make sure to install Virtualenv using the following command:

C:\Python27\python -m pip install virtualenv

Populate the Jira.jql file with the JQL that will result in Jira tickets that you want to examine.

# Run.bat
The run.bat batch file is provided for convenience.

# Tools
The following tools have been implemented.

## FindTicketsWithoutMergedTo
The FindTicketsWithoutMergedTo script searches Jira tickets based on a given JQL and returns the ones that have
no "Merged to" relationship."


