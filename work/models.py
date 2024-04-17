from django.db import models

# Create your models here.

class Genre(models.Model):
    genreName       =   models.CharField(max_length=100,unique=True)
    description     =   models.CharField(max_length=100)

class Movies(models.Model):
    title           =   models.CharField(max_length=100)
    release_date    =   models.DateField(auto_now_add = True)
    duration        =   models.TimeField()
    summary         =   models.CharField(max_length=200)
    GenreName       =   models.ForeignKey(Genre,on_delete=models.CASCADE,to_field='genreName')

    def __str__(self):
        return self.title