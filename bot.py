# -*- coding: utf-8 -*-
"""
Python Slack Bot class for use with the pythOnBoarding app
"""
import os
#import message

from slackclient import SlackClient


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
# our bots name
BOT_NAME = 'alpha5'
# our bots ID
# we store it as an environment variable
# export BOT_ID='bot id returned by script'
BOT_ID = os.environ["BOT_ID"]


if __name__ == "__main__":
    # This is how we retrieve our bot id
    api_call = sc.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)


    # Send text to channel
    # comment it out to avoid spam
    # sc.api_call(
    #   "chat.postMessage",
    #   channel="#pro_bot-test",
    #   text="Hello from alpha5 bot this is a test! :tada:",
    #   thread_ts="1476746830.000003"
    # )

    # retrieve the channel list
    # print(sc.api_call("channels.list", exclude_archived=1))

    # get the groups user lists
    #print(sc.api_call('users.list'))
    print(sc.api_call('users.list'))
