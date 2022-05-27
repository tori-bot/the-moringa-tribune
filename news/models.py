from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    @classmethod
    def display_editors(cls,self):
        first_name=self.first_name
        last_name=self.last_name
        email=self.email
        return first_name,last_name,email

    @classmethod
    def update_editor(cls,self):
        first_name=self.append.first_name
        last_name=self.append.last_name
        email=self.append.email
        return first_name,last_name,email   

    def __str__(self):
        return self.first_name

class tags(models.Model):
    name=models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length =60)
    post= models.TextField()
    editor=models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags=models.ManyToManyField(tags)
    
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