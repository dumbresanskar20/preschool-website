from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_page(request):
    """Contact page with form and info."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '📩 Your message has been sent! We will get back to you soon.'
            )
            return redirect('contact:page')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
        'page_title': 'Contact Us',
    })
