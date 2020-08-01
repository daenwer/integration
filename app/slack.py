import requests
from integration.settings_slack import *


def slack_post_msg(message):
    data = {
        "text": message,
    }
    requests.post(url=SLACK_URL, json=data)


def create_new_task(*args, **kwargs):
    description = args[0]
    print(description)
    return 'something'


if __name__ == '__main__':
    text = 'Hello from pycharm!!!!)'

    slack_post_msg(text)
