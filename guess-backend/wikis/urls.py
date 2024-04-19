from django.urls import path

from . import views

# maps URLS to functions in views
urlpatterns = [
    path('get-page-data/', views.get_page_data, name='get_page_data'),
    path('add-score/', views.add_score, name='add_score'),
    path('send-stats/', views.send_stats, name='send_stats'),
]
