import requests
import json
for i in range(1, 15):
    response = requests.get('https://stword.com/api/posts/12/words?page=' + str(i))
    data = json.loads(response.text)
    for value in (data['data']['items']):
        print(value['description'])