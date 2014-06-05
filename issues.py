from redmine import Redmine

server = Redmine('http://demo.redmine.org/')

def issue(redmine_issue):
    i = {
         'subject': redmine_issue.subject,
         'priority': redmine_issue.priority.name if redmine_issue.priority else None,
         'author': redmine_issue.author.name if redmine_issue.author else None,
         'assigned_to': redmine_issue.assigned_to.name if redmine_issue.assigned_to else None,
         'project': redmine_issue.project.name if redmine_issue.project else None,
         'id': redmine_issue.id,
    }
    return i

def get_issues(project_names):
    issues = []
    
    for project_name in project_names:
        print project_name
        project = server.projects.get(project_name)
        issues.extend(
            [issue(i) for i in project.issues()]
        )
    return issues