from django.shortcuts import render,redirect
from django.http import HttpResponse
from data.models import Comment
from .models import Article
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def about(request):
    return render(request, 'about.html')

def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request, 'article_list.html', {'articles':articles})

@login_required(login_url="data/login/")
def article_details(request, slug):
    #return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', {'article':article})


@login_required(login_url="/data/login/")
def article_create(request):
      if request.method=='POST':
         form=forms.CreateArticle(request.POST, request.FILES)
         if form.is_valid():
             #save article to db
             form.save()
             return redirect('users:list')   
      else:     
        form=forms.CreateArticle()
      return render(request, 'article_create.html', {'form':form})