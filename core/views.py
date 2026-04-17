from django.shortcuts import render
from reviews.models import Review
from gallery.models import GalleryImage


def home(request):
    """Main landing page view."""
    reviews = Review.objects.filter(is_approved=True).order_by('-rating', '-created_at')[:5]
    gallery_images = GalleryImage.objects.filter(is_active=True)[:8]
    context = {
        'reviews': reviews,
        'gallery_images': gallery_images,
        'page_title': 'Rainbow Preschool & Bunnyland Preschool',
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About us page."""
    return render(request, 'core/about.html', {'page_title': 'About Us'})


def activities(request):
    """Activities page."""
    return render(request, 'core/activities.html', {'page_title': 'Our Activities'})
