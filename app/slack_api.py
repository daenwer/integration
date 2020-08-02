import requests
from integration.settings_slack import *
from app.jira_api import create_new_task_jira


def slack_post_msg(message):
    data = {
        "text": message,
    }
    requests.post(url=SLACK_URL, json=data)


def create_new_task(*args, **kwargs):
    description = args[0]
    number_task = create_new_task_jira(description)
    return number_task.key

