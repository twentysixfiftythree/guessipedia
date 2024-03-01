from django.db import models

# Create your models here.


class WikiPage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    surrounding_links = models.TextField()
    link = models.CharField(max_length=100)
    categories = models.TextField()

    def __str__(self):
        return self.title
