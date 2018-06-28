from jira.client import JIRA

class MyJira():
    """
    The StrozJira class encapsulates the necessary methods to interact with 
    the Jira server.
    
    This library relies solely on the jira-python library. More information on 
    the library is located here https://jira.readthedocs.io/en/master/index.html.
    """
    
    def __init__(self, url = "http://myjiraurl:8080", username="myuser", password="myuserpassword"):
        self.options = {'server': url}
        self.connection = JIRA(self.options, basic_auth= (username, password))
        
    def get_fix_version(self,key):
        return True
    
    def get_issuelinks(self,key):
        return self.connection.issue(key).fields.issuelinks # Enumerate Links
                        
    def get_merge_to_link_issues(self, key):
        _merge_to_issues=[]
        issuelinks = self.connection.issue(key).fields.issuelinks # Enumerate Links
        for _link in issuelinks: # Loop through issue links
            _props = dir(_link) # Get attributes of link property to determine if issue has merge to link
            if (_link.type.name == "Code Merge") and ('outwardIssue' in _props):
                _merge_to_issues.append(_link.outwardIssue.key)
        return _merge_to_issues
    
    def has_mergeto_issue(self, key):
        _has_mergeto_ticket = False;
        _issuelinks = self.connection.issue(key).fields.issuelinks # Enumerate Links
        for _link in _issuelinks: # Loop through issue links
            _props = dir(_link) # Get attributes of link property to determine if issue has merge to link
            if (_link.type.name == "Code Merge") and ('outwardIssue' in _props):
                _is_merged_to_key = _link.outwardIssue.key
                _has_mergeto_ticket=True
        return _has_mergeto_ticket
    
    def simple_search(self, searchstr):
        return self.connection.search_issues(searchstr)
        
