"""
URL configuration for Rainbow Preschool project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('enquiry/', include('enquiry.urls')),
    path('reviews/', include('reviews.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),
    path('gallery/', include('gallery.urls')),
]

# Ensure media files (user uploads) are served even when DEBUG = False for Render
from django.urls import re_path
from django.views.static import serve
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom admin site header
admin.site.site_header = "🌈 Rainbow & Bunnyland Preschool Admin"
admin.site.site_title = "Preschool Admin Portal"
admin.site.index_title = "Welcome to Admin Dashboard"
