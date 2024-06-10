from django.db import models

# Create your models here.


class WikiPage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    surrounding_links = models.TextField()
    surrounding_titles = models.TextField()
    link = models.CharField(max_length=100)
    categories = models.TextField()

    def __str__(self):
        return self.title


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField()
