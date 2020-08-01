from atlassian import Jira
from integration.settings_jira import *


def create_something():
    jira = Jira(
         url=JIRA_URL,
         username=JIRA_USERNAME,
         password=JIRA_PASSWORD
    )

    jira.issue_create(fields={
        'project': {'key': 'TEST'},
        'issuetype': {
            "name": "Task"
        },
         'summary': 'test rest',
         'description': 'rest rest',
    })


if __name__ == '__main__':
    create_something()
