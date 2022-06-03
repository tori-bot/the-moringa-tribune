from django.db import models
import datetime as dt
from django.contrib.auth.models import User



class Tags(models.Model):
    name=models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title=models.CharField(max_length =60)
    post= models.TextField()
    # the tinymce editor saves the input as raw html to the database.
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tags)
    
    pub_date=models.DateTimeField(auto_now_add=True)
    article_image=models.ImageField(upload_to='articles/',null=True)
    # article_image=models.ImageField(upload_to='articles/',default='default.png')

    @classmethod
    def todays_news(cls):
        today=dt.date.today()
        news=cls.objects.filter(pub_date__date=today)
        #date filter converts datetimefield to a date...double underscores are meant to define query filters. in this case the filter is date
        return news

    @classmethod
    def days_news(cls,date):
        news=cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news=cls.objects.filter(title__icontains=search_term)
        # We filter the model data using the __icontains query filter. This filter will check if any word in the titlefield of our articles matches the search_term.
        return news

    def __str__(self):
        return self.title

class NewsLetterRecipients(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()