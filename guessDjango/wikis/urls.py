from django.urls import path

from . import views

# maps URLS to functions in views
urlpatterns = [
    path('get-page-data/', views.get_page_data, name='get_page_data'),
]
