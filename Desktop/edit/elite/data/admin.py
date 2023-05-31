from django.contrib import admin
from.models import User
from.models import Comment
from.models import Book

# Register your models here.
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Book)
