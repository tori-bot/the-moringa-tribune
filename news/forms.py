from django import forms
from .models import Article

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(max_length=30,label='First name')
    email=forms.EmailField(label='Email')
    
class NewsArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        excludes=['editor','pub_date']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }