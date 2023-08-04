import os
import logging
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk.web import WebClient
from operator import itemgetter
from views import TestBlock

DEFAULT_VALUES = {
    'SLACK_PORT': 3000,
    'ENV': 'development'
}

# access environment variables
load_dotenv()
SLACK_PORT, ENV = itemgetter('SLACK_PORT', 'ENV')({ **DEFAULT_VALUES, **dict(os.environ) })

# Slack APP
slack_app = App()

# In memory storage for illustration purposes
db = {}

def onboard(user_id: str, channel: str, client: WebClient):
    test_block = TestBlock(channel)

    # Get the message payload
    message = test_block.get_message_payload()

    # Post the message in Slack
    response = client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed a task.
    test_block.timestamp = response["ts"]

    # Save the message sent to in memory "DB"
    if channel not in db:
        db[channel] = {}
    db[channel][user_id] = test_block

    # ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.

# Note: Bolt provides a WebClient instance as an argument to the listener function
# we've defined here, which we then use to access Slack Web API methods like conversations_open.
# For more info, checkout: https://slack.dev/bolt-python/concepts#message-listening
@slack_app.event("team_join")
def handle_message(event, client):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # Get the id of the Slack user associated with the incoming event
    user_id = event.get("user", {}).get("id")

    # Open a DM with the new user.
    response = client.conversations_open(users=user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    onboard(user_id, channel, client)


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@slack_app.event("reaction_added")
def update_emoji(event, client):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("item", {}).get("channel")
    user_id = event.get("user")

    if channel_id not in db:
        return

    # Get the original tutorial sent.
    test_block = db[channel_id][user_id]

    # Mark the reaction task as completed.
    test_block.reaction_task_completed = True

    # Get the new message payload
    message = test_block.get_message_payload()

    # Post the updated message in Slack
    updated_message = client.chat_update(**message)
    print(updated_message)


# =============== Pin Added Events ================ #
# When a users pins a message the type of the event will be 'pin_added'.
# Here we'll link the update_pin callback to the 'pin_added' event.
@slack_app.event("pin_added")
def update_pin(event, client):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("channel_id")
    user_id = event.get("user")

    # Get the original tutorial sent.
    test_block = db[channel_id][user_id]

    # Mark the pin task as completed.
    test_block.pin_task_completed = True

    # Get the new message payload
    message = test_block.get_message_payload()

    # Post the updated message in Slack
    updated_message = client.chat_update(**message)
    print(updated_message)


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_app.event("message")
def message(event, client):
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if text and text.lower() == "start":
        return onboard(user_id, channel_id, client)
    
if __name__ == "__main__":
    if ENV == 'development':
        print('Start slack app in DEV mode')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler())
        slack_app.start(SLACK_PORT)
    else:
        print('TODO: Run slack app in PROD mode')
