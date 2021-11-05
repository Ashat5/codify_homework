"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from about.views import get_about_data
from article.views import article_create
from main.views import index
from django.conf.urls.static import static
from blog import settings
from article.views import article_show
from comment.views import create_comment



urlpatterns = [
    path('about/', get_about_data, name='about_data'),
    path('article/create', article_create, name='article_create'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:page>', index, name='index'),
    path('article_show/<int:id>/', article_show, name='article_show'),
    path('article/<int:article_id>/comment/create', create_comment, name='create_comment')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
