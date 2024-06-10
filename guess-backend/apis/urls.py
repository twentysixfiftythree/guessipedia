from django.urls import path

from . import views

# maps URLS to functions in views
urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
]
