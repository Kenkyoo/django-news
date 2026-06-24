from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here. 
def index(request):
    
    newsapi = NewsApiClient(api_key ='04b80be27a71435480b00af981af7e6d')
    top = newsapi.get_top_headlines(
        sources='techcrunch',
        language='en',
        page_size=12  # Limitar cantidad de noticias
    )

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context ={"mylist":mylist})