from django.shortcuts import render
from pyexpat.errors import messages

from .forms import ApplicationForm
from .models import Form
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date = request.POST.get('available_date')
        occupation = request.POST.get('occupation')


        Form.objects.create(first_name = first_name, last_name = last_name,
                            email = email, date = date, occupation = occupation)

        message_body = f"A new job application was submitted. Thank You, {first_name}."
        email_message = EmailMessage("Form Submission Confirmation", message_body,to=[email])
        email_message.send()

    return render(request,"index.html")

