# Problem description
# Find out if there are any duplicate urls used in the
# json placeholder photo data

import requests

url = 'https://api.duckduckgo.com'

def test_ddg0():
    response = requests.get(url + '/?q=DuckDuckGo&format=json')
    response_data = response.json()
    assert "DuckDuckGo" in response_data["Heading"]

