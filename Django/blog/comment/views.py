from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment

def create_comment(request, article_id):
    if request.method == 'POST':
        print('+')
        comment_form = CommentForm(request.POST)
        print('-')
        if comment_form.is_valid():
            comment_object = Comment()
            comment_object.save()
            print('saved')
    comment = Comment.objects.all()
    comments = Comment.objects.filter(article__id=article_id)
    return render(request, 'article_show.html')

