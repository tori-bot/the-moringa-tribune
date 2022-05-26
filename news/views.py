import re
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models  import Article
import datetime as dt


# Create your views here.
def welcome(request):
    #request param contains info of current web request that triggered this view
    return render(request, 'welcome.html')
    # return HttpResponse('Welcome to The Moringa Tribune')

def news_today(request):
    date=dt.date.today()
    #call the date.today function to get the current date. 
    news=Article.todays_news()

    return render(request, 'all_news/today_news.html',{'date':date,'news':news} )

def convert_dates(dates):
    # function gets weekday number for the date.
    day_number=dt.date.weekday(dates)
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #returns actual day of the week
    day=days[day_number]
    return day

def past_days_news(request,past_date):
    
    try:
        #convert data fromstring url 
        date=dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date==dt.date.today():
        return redirect(news_today)

    news=Article.days_news(date)

    return render(request, 'all_news/past_news.html',{'date':date,'news':news} )

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        #check if the article query exists in our request.GET object and then we then check if it has a value.
        search_term=request.GET.get('article')
        searched_articles=Article.search_by_title(search_term)
        #call the search_by_title class method and pass in the user input
        message=f'{search_term} '
        return render(request,'all_news/search.html',{'message':message,'articles':searched_articles} )
    else:
        message='You have not searched for any item'
        return render(request,'all_news/search.html',{'message':message} )

def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request,'all_news/article.html',{'article':article} )