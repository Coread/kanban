from redmine import Redmine
from redmine_settings import server

server = Redmine(server['url'], username=server['username'], password=server['password'])


COLUMN_STATE_MAP = {
    'Reviewed': 'col_todo',
    'New': 'col_todo',
    'Closed': 'col_done',
    'Feedback': 'col_done',
    'Verify': 'col_done',
    }


def issue(redmine_issue):
    i = {
         'subject': redmine_issue.subject,
         'priority': redmine_issue.priority.name if redmine_issue.priority else 'None',
         'author': redmine_issue.author.name if redmine_issue.author else 'None',
         'assigned_to': redmine_issue.assigned_to.name if redmine_issue.assigned_to else 'None',
         'project': redmine_issue.project.name if redmine_issue.project else 'None',
         'id': redmine_issue.id,
         'status': redmine_issue.status.name if redmine_issue.status else 'None',
    }
    i['col'] = COLUMN_STATE_MAP[i['status']]
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
