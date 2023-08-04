# Example of making calls internally to the flask service

from requests import get

# Change to be dynamic from env
url_template = "http://127.0.0.1:5000"

async def get_timestamp():
  res = await get(url_template + "/api/timestamp")
  print(res)
  json = res.json()
  print(json)
  return f"{json.time}"

