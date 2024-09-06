from django.shortcuts import render , HttpResponse

# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            # # Redirect to a thank-you page or a success message
            # return redirect('contact_success')  # Define this URL in your urls.py
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    render(request , 'Contact_success.html')


# Create your views here.
def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'About.html')

def skills(request):
    return render(request , 'Skills.html')

