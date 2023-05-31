from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment, Book
from . import forms
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout


# Create your views here.
@login_required(login_url="data:login")
def create_book(request):
    if request.method=='POST':
         form=forms.BookForm(request.POST)
         if form.is_valid():
             #save article to db
             form.save()
             return redirect('data:create_book')   
    else:     
        form=forms.BookForm()
    return render(request, 'addbook.html', {'form': form})



def create_comment(request):
   if request.method=='POST':
      form=forms.Comment_form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('data:commentlist')
    
   else:
      form=forms.Comment_form()
      return render(request, 'comment_create.html', {'form': form})
        
def comment_list(request):
   comments=Comment.objects.all()
   return render(request, 'commentlist.html', {'comments':comments})

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log in user
            login(request, user)
            return redirect('users:list')
    else:
     form=UserCreationForm()
    return render (request, 'signup.html', {'form': form})

def login_view(request):

    if request.method=='POST':
       form=AuthenticationForm(data=request.POST)     
       if form.is_valid():
        #logging in user
        user=form.get_user()
        login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
         return redirect('users:list')
    

    else:
        form=AuthenticationForm()
    return render(request,  'login.html',{'form':form})

def logout_view(request):
    #if request.method=='POST':
        logout(request)
        return redirect('users:list')

@login_required(login_url="data:login")
def booklist_view(request):
    books=Book.objects.all().order_by('date')
    return render(request, "booklist.html", {'books':books})