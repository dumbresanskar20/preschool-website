from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm


def enquiry_submit(request):
    """Handle enquiry form submission."""
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '🎉 Thank you! Your enquiry has been submitted successfully. '
                'We will contact you within 24 hours!'
            )
            return redirect('enquiry:success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EnquiryForm()
    return render(request, 'enquiry/enquiry_form.html', {
        'form': form,
        'page_title': 'Enroll Your Child',
    })


def enquiry_success(request):
    """Success page after enquiry submission."""
    return render(request, 'enquiry/success.html', {
        'page_title': 'Enquiry Submitted Successfully',
    })
