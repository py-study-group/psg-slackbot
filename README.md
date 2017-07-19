# Here is the link to the official guide

[Official repository/guide](https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/README.md#pythonboarding-bot)

# Setting up your environment

```
$ virtualenv slackblot -p python3
```

# Install required packages
```
$ pip install -r requirements.txt
```
You may need sudo if you are not using virtual environment

# Tokens and Authentication

```
$ export SLACK_API_TOKEN='your slack token pasted here'
```

[Follow the instructions on this link to get the token](http://python-slackclient.readthedocs.io/en/latest/auth.html)

# Create get_bot_id.py

This file will contain the bot logic and actions
Run the script so you can get the bot id and then

```
$ export BOT_ID='your bot id pasted here'
```

# Create message.py

This file contains a python class for creating message objects. Creating message objects allows us to store information about each onboarding message our bot sends out to various new users and more easily keep track of what tasks each user has completed

# TODO

1. bot to send message as alpha5 and not as a simple bot
2. Message new members


# Articles that helped me
[build-first-slack-bot](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
[direct messages with bot](https://medium.com/@julianmartinez/how-to-write-a-slack-bot-with-python-code-examples-4ed354407b98)
