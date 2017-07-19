# -*- coding: utf-8 -*-
"""
Python Slack Bot
"""
import os

from slackclient import SlackClient


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
# our bots name
BOT_NAME = 'alpha5'
# our bots ID
# we store it as an environment variable
# export BOT_ID='bot id returned by script'
#BOT_ID = os.environ["BOT_ID"]


if __name__ == "__main__":
    # This is how we retrieve our bot id
    api_call = sc.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                # here we get the bot id
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
