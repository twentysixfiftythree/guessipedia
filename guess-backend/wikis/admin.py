from django.contrib import admin

from .models import Score, WikiPage

# Register your models here.

admin.site.register(WikiPage)

admin.site.register(Score)
