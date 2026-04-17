from django.urls import path
from . import views

app_name = 'enquiry'

urlpatterns = [
    path('submit/', views.enquiry_submit, name='submit'),
    path('success/', views.enquiry_success, name='success'),
]
