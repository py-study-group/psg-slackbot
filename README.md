#Here is the link to the official guide
[Official repository/guide](https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/README.md#pythonboarding-bot)

#Setting up your environment
```
$ virtualenv slackblot -p python3
```

#Install slackclient
```
$ pip install slackclient
```
You may need sudo if you are not using virtual environment

#Tokens and Authentication
```
$ export SLACK_API_TOKEN='your slack token pasted here'
```
[Follow the instructions on this link to get the token](http://python-slackclient.readthedocs.io/en/latest/auth.html)

#Create bot.py
This file will contain the bot logic and actions

#Create message.py
This file contains a python class for creating message objects. Creating message objects allows us to store information about each onboarding message our bot sends out to various new users and more easily keep track of what tasks each user has completed

#TODO
1. bot to send message as alpha5 and not as a simple bot
2. Message new members



#Articles that helped me
[build-first-slack-bot](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)