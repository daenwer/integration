import requests
import integration.settings as settings


def slack_post_msg(message):
    data = {
        "text": message,
    }
    requests.post(url=settings.SLACK_URL, json=data)


if __name__ == '__main__':
    text = 'Hello from pycharm!!!!)'
    slack_post_msg(text)
