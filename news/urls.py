from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



# create URL instances by calling the url function. We pass in the URL regular expression the view and a name keyword argument.
urlpatterns =[
    url(r'^$',views.news_today,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$ ',views.past_days_news,name='pastNews'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^article/(\d+)',views.article,name='article')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
# urlpatterns =[
    # path('',views.welcome,name='welcome'),
    #path('',views.news_today,name='news_today'),
    #path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name='pastNews')
    #path('search/',views.search_results,name='search_results')

# ]