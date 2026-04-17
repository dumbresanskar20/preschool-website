from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Dashboard CRUD APIs
    path('dashboard/api/enquiry/', views.api_enquiry, name='api_enquiry'),
    path('dashboard/api/review/', views.api_review, name='api_review'),
    path('dashboard/api/message/', views.api_message, name='api_message'),
    path('dashboard/api/gallery/', views.api_gallery, name='api_gallery'),
]
