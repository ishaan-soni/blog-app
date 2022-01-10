from django.urls import path
from .views import ContactView, download_resume
from contact import views

app_name = 'contact'

urlpatterns = [
    path('',ContactView.as_view(),name='contactview'),
    
]