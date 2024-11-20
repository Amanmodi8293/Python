import requests
import json
query = input("What type of news are you intrested in ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-19&sortBy=publishedAt&apiKey=c4a50c48627e40cbb1bd0bbb819f0a4e"
 
res = requests.get(url)

news = json.loads(res.text)
# print(news, type(news))

for article in news["articles"]:
    print(f"Title : {article['title']}")
    print(f"Description : {article['description']}")
    print("___________________________________________________________________")