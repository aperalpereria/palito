import requests
import json


def send_slack_message(message):
    requests.post(
        "https://hooks.slack.com/services/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",
        json.dumps(
            {
                "text": message
            }
        )
    )