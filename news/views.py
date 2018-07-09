from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    try:
        
        date = dt.date.today()
    except ValueError:
        raise Http404()
    return render(request,'all-news/today-news.html', {"date":date,})

# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-news/past-news.html', {"date": date}) 
            
