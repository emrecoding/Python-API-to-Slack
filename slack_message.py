import pprint
import requests
from digital_ocean_status import digital_ocean_status
from slack_status import slack_status
from github_status import github_status
pp = pprint.PrettyPrinter(indent=4)
def slack_message(data):
    url = 'https://hooks.slack.com/services/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'
    header = {"Content-type": "application/json"}
    data = {"text": "This a test from Merdan",
            "attachments": [
                {"slack": slack_status()},
                {"github": github_status()},
                {"digital_ocean": digital_ocean_status()}
            ]
    }
    slack_resp = requests.post(url, headers=header, json=data)
    print(slack_resp)
