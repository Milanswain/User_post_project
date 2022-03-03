
from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    username=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Post(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    



