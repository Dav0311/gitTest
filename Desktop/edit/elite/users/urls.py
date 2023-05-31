from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='users'

urlpatterns  =[
    path('', views.article_list, name="list"),
    path('about/', views.about, name="about"),
    path('create/', views.article_create, name="create"),
    path('article/<slug:slug>/', views.article_details, name='detail'),
]


urlpatterns += staticfiles_urlpatterns()

