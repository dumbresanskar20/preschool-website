from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from enquiry.models import Enquiry
from reviews.models import Review
from contact.models import ContactMessage
from gallery.models import GalleryImage

def is_staff_member(user):
    return user.is_staff or user.is_superuser

def user_login(request):
    if request.user.is_authenticated and is_staff_member(request.user):
        return redirect('accounts:dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if is_staff_member(user):
                auth_login(request, user)
                return JsonResponse({'success': True, 'redirect_url': '/accounts/dashboard/'})
            else:
                return JsonResponse({'success': False, 'message': "Only staff members can access the dashboard."})
        else:
            return JsonResponse({'success': False, 'message': "Invalid username or password."})
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {
        'form': form,
        'page_title': 'Staff Login'
    })

def user_logout(request):
    auth_logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('core:home')

@login_required
@user_passes_test(is_staff_member, login_url='accounts:login')
def dashboard(request):
    context = {
        'page_title': 'Staff Dashboard',
        'enquiries': Enquiry.objects.all(),
        'reviews': Review.objects.all(),
        'contact_messages': ContactMessage.objects.all(),
        'gallery_images': GalleryImage.objects.all(),
        'total_enquiries': Enquiry.objects.count(),
        'total_pending_reviews': Review.objects.filter(is_approved=False).count(),
        'total_unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'total_gallery': GalleryImage.objects.count(),
    }
    return render(request, 'accounts/dashboard.html', context)

# --- API CRUD Views (Expect Form Data via POST) ---

@login_required
@user_passes_test(is_staff_member)
@require_POST
def api_enquiry(request):
    action = request.POST.get('action')
    pk = request.POST.get('id')
    
    if action == 'delete':
        Enquiry.objects.filter(id=pk).delete()
        messages.success(request, 'Enquiry deleted successfully.')
    elif action == 'add':
        Enquiry.objects.create(
            parent_name=request.POST.get('parent_name'),
            child_name=request.POST.get('child_name'),
            child_age=request.POST.get('child_age'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            message=request.POST.get('message', ''),
            is_read=request.POST.get('is_read') == 'on'
        )
        messages.success(request, 'Enquiry added successfully.')
    elif action == 'edit':
        enq = Enquiry.objects.filter(id=pk).first()
        if enq:
            enq.parent_name = request.POST.get('parent_name')
            enq.child_name = request.POST.get('child_name')
            enq.child_age = request.POST.get('child_age')
            enq.phone = request.POST.get('phone')
            enq.email = request.POST.get('email')
            enq.message = request.POST.get('message', '')
            enq.is_read = request.POST.get('is_read') == 'on'
            enq.save()
            messages.success(request, 'Enquiry updated successfully.')
            
    return redirect('/accounts/dashboard/?tab=enquiries')

@login_required
@user_passes_test(is_staff_member)
@require_POST
def api_review(request):
    action = request.POST.get('action')
    pk = request.POST.get('id')
    
    if action == 'delete':
        Review.objects.filter(id=pk).delete()
        messages.success(request, 'Review deleted successfully.')
    elif action == 'add':
        Review.objects.create(
            parent_name=request.POST.get('parent_name'),
            child_name=request.POST.get('child_name'),
            rating=request.POST.get('rating'),
            review_message=request.POST.get('review_message'),
            is_approved=request.POST.get('is_approved') == 'on'
        )
        messages.success(request, 'Review added successfully.')
    elif action == 'edit':
        rev = Review.objects.filter(id=pk).first()
        if rev:
            rev.parent_name = request.POST.get('parent_name')
            rev.child_name = request.POST.get('child_name')
            rev.rating = request.POST.get('rating')
            rev.review_message = request.POST.get('review_message')
            rev.is_approved = request.POST.get('is_approved') == 'on'
            rev.save()
            messages.success(request, 'Review updated successfully.')
            
    return redirect('/accounts/dashboard/?tab=reviews')

@login_required
@user_passes_test(is_staff_member)
@require_POST
def api_message(request):
    action = request.POST.get('action')
    pk = request.POST.get('id')
    
    if action == 'delete':
        ContactMessage.objects.filter(id=pk).delete()
        messages.success(request, 'Message deleted successfully.')
    elif action == 'add':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            is_read=request.POST.get('is_read') == 'on'
        )
        messages.success(request, 'Message added successfully.')
    elif action == 'edit':
        msg = ContactMessage.objects.filter(id=pk).first()
        if msg:
            msg.name = request.POST.get('name')
            msg.email = request.POST.get('email')
            msg.phone = request.POST.get('phone', '')
            msg.subject = request.POST.get('subject')
            msg.message = request.POST.get('message')
            msg.is_read = request.POST.get('is_read') == 'on'
            msg.save()
            messages.success(request, 'Message updated successfully.')
            
    return redirect('/accounts/dashboard/?tab=messages')

@login_required
@user_passes_test(is_staff_member)
@require_POST
def api_gallery(request):
    action = request.POST.get('action')
    pk = request.POST.get('id')
    
    if action == 'delete':
        GalleryImage.objects.filter(id=pk).delete()
        messages.success(request, 'Image deleted successfully.')
    # Add/Edit omitted for gallery file uploads in this simple API (could be added if needed, 
    # but the problem only explicitly stressed full CRUD on Enquiry context. We will add a basic add/edit without file overwrite for edit).
    elif action == 'add':
        image_file = request.FILES.get('image')
        if image_file:
            GalleryImage.objects.create(
                title=request.POST.get('title'),
                category=request.POST.get('category'),
                image=image_file,
                is_active=request.POST.get('is_active') == 'on'
            )
            messages.success(request, 'Image added successfully.')
    elif action == 'edit':
        img = GalleryImage.objects.filter(id=pk).first()
        if img:
            img.title = request.POST.get('title')
            img.category = request.POST.get('category')
            new_img = request.FILES.get('image')
            if new_img:
                img.image = new_img
            img.is_active = request.POST.get('is_active') == 'on'
            img.save()
            messages.success(request, 'Image details updated.')
            
    return redirect('/accounts/dashboard/?tab=gallery')
