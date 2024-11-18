from django.urls import path
from timetable_app.views import HomeView

# my urls 
urlpatterns = [
    path('', HomeView.as_view(), name='index')
]