import sys
from strozjira import StrozJira

jira = MyJira()

# Read the Jira sql from a file called Jira.sql
try:
    jql = "Jira.jql"
    fp = open(jql,'r')
    searchStr= fp.readline()
    fp.close()  
except IOError as e:
    print "Unable to find JQL file, " + jql + ". {0}.".format(e.strerror)
    exit(1)

try:
    issues = jira.simple_search(searchStr) # Search Jira using given JQL

except:
    print "Jira search failed. Check your JQL syntax."
    exit(1)

issue_keys = [issue.key for issue in issues] # Get all issue keys in a list
for issue in issues: # Loop through the list of issues
    found_merge_ticket=False;

    issuelinks = jira.get_issuelinks(issue.key)
    for link in issuelinks: # Loop through issue links
        props = dir(link) # Get attributes of link property to determine if issue has merge to link
        if (link.type.name == "Code Merge") and ('outwardIssue' in props):
            is_merged_to_key = link.outwardIssue.key
            found_merge_ticket=True
    if not found_merge_ticket:
        sys.stdout.write(issue.key + ",")
       
sys.stdout.flush()