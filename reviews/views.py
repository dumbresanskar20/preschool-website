from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """Display all approved reviews."""
    reviews = Review.objects.filter(is_approved=True).order_by('-rating', '-created_at')[:5]
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'page_title': 'Parent Reviews',
    })


def review_submit(request):
    """Handle review form submission."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '⭐ Thank you for your review! It will be visible after admin approval.'
            )
            return redirect('reviews:success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {
        'form': form,
        'page_title': 'Write a Review',
    })


def review_success(request):
    """Success page after review submission."""
    return render(request, 'reviews/success.html', {
        'page_title': 'Review Submitted',
    })
