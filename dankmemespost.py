import json
import requests


def get_reddit_post():
  response = requests.get(
    "https://reddit.com/r/dankmeme/random.json",
    headers={'User-agent': 'python:random.reddit.post:v1.0'})
  data = json.loads(response.text)
  url = data[0]["data"]["children"][0]["data"]["url_overridden_by_dest"]
  type = data[0]["data"]["children"][0]["data"]["secure_media"]
  thumbnail = data[0]["data"]["children"][0]["data"]["thumbnail"]
  permalink = "https://reddit.com" + data[0]["data"]["children"][0]["data"][
    "permalink"]

  return url, permalink, type, thumbnail
