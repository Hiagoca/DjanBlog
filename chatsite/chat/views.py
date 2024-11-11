from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')
def news(request):
    return render(request, 'chat/news.html')