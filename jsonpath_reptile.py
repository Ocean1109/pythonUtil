import os
import urllib.request
import json
import jsonpath

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('douban.json', 'w', encoding='utf-8')as fp:
    fp.write(content)

obj = json.load(open('douban.json', 'r', encoding='utf-8'))
os.remove('douban.json')
movie_list = jsonpath.jsonpath(obj, '$.subjects[*].title')
print(movie_list)
