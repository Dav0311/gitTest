from django.db import models
from users.models import Article

# Create your models here.
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    author =models.ForeignKey(Article, related_name="comments", default=None, on_delete=models.CASCADE, null=True)
    created_date =models.DateTimeField(auto_now_add=True)
    body=models.CharField(max_length=300)

    def __str__(self):
        return '%s-%s' % (self.title, self.body)

  

class Book(models.Model):

    SERVICE_CHOICES=[
        ("C","CONFERENCE HALL"),
        ("A","ACCOMMODATION"),
        ("E", "EVENT HALL"),
    ]

    PAYMENT_CHOICES=[
        ("C","CASH"),
        ("A","CREDIT CARD"),
        ("B", "CHEQUE"),
    ]

    name=models.ForeignKey(User, on_delete=models.CASCADE)
    checkin=models.DateField()
    checkout=models.DateField()
    payment=models.CharField(max_length=1, choices=PAYMENT_CHOICES, default="A")
    service=models.CharField(max_length=1, choices=SERVICE_CHOICES, default="A")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service
