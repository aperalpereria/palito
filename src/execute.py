import json
import slack
import random

candidates = json.loads(open('../config/candidates-default.json').read())
number_of_candidates = len(candidates)
chosen_candidate = random.randint(0,number_of_candidates-1)
slack.send_slack_message(f"{candidates[chosen_candidate]['name']} ha sido elegido!")
