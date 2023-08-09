#!/bin/bash

# Get user specific ngrok URL + PORT (must be same as slack app server)
source .env
P="$SLACK_PORT"
PORT="${P:=3000}"

ngrok http --domain=selected-"$NGROK_URL" "$PORT"
