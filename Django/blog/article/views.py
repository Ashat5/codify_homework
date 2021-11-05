from django.shortcuts import render
from article.form import ArticleCreateForm
from article.models import Article
from comment.forms import CommentForm
from comment.models import Comment

def article_create(request):
    if request.method == 'POST':
        print('Create')
        article_form = ArticleCreateForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            print('Saved')
        else:
            print('Errors')
            return render(request, 'article_create.html', {'form': article_form, 'error': article_form.errors})   
    form = ArticleCreateForm()
    return render(request, 'article_create.html', {'form' : form})

def article_show(request, id):
    article_object = Article.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        print(comment_form)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            comment_object = Comment(name=cd['name'], text=cd['text'], article=article_object)
            comment_object.save()
            print('saved')
        else:
            print('error')
    comment_object = Comment.objects.filter(article = article_object)
    comments_count = comment_object.count()
    print(comments_count)
    # print(comment_object)
    return render(request, 'article_show.html', {'article': article_object, 'form': form, 'comments': comment_object, 'count':
    comments_count}) 

            

