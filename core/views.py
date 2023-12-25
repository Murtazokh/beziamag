from django.shortcuts import render, redirect
from .models import Contact, About, Testimonial
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .models import About, Testimonial

def home(request):
    return render(request, 'pages/homepage.html')

def about(request):
    about_content = About.objects.first()  # Assuming you only have one about instance
    return render(request, 'pages/about.html', {'about': about_content})

def testimonials(request):
    testimonials_list = Testimonial.objects.filter(visible=True)
    return render(request, 'pages/testimonials.html', {'testimonials': testimonials_list})

def contact(request):
    if request.method == 'POST':
        # handle the form submission
        contact_data = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact_data.save()

        # Send an email notification (you need to configure EMAIL_* settings in settings.py)
        # send_mail(
        #     contact_data.subject,
        #     contact_data.message,
        #     settings.EMAIL_HOST_USER,
        #     [settings.EMAIL_HOST_USER],
        #     fail_silently=False,
        # )
        
        # Redirect to a new URL after POST
        return redirect('core:contact_confirm')

    # Show initial contact form
    return render(request, 'pages/contact.html')

def contact_confirm(request):
    return render(request, 'pages/contact-confirm.html')