from django.shortcuts import render
from .models import GalleryImage


def gallery_view(request):
    """View to display the gallery of preschool images."""
    images = GalleryImage.objects.filter(is_active=True).order_by('-uploaded_at')
    
    # Optional: Filter by category if passed in request
    category = request.GET.get('category')
    if category:
        images = images.filter(category=category)
        
    return render(request, 'gallery/gallery.html', {
        'images': images,
        'page_title': 'Photo Gallery',
        'current_category': category,
    })
