from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='data'

urlpatterns  =[
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('review/', views.create_comment, name="create_comment"),
    path('books/', views.booklist_view, name='booklist'),
    path('create_book/', views.create_book, name='create_book'),
    path('comments/', views.comment_list, name='commentlist'),
]