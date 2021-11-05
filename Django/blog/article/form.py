from django import forms
from django import forms
from article.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('created_date', 'updated_date')
