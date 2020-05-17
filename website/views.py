from django.shortcuts import render, redirect
from .models import College
from .forms import UserForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'website/home.html', {})


def donate(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            college = College.objects.all().filter(name=form.cleaned_data.get('college_name'))[0]
            required_email_ext = college.college_ext
            email = form.cleaned_data.get('email')
            email_ext = email.split('@')[1]
            print(required_email_ext, email_ext)
            if required_email_ext == email_ext:
                subject = 'Subject'
                message = "Here's a form :" + college.form_donate
                to_email = list(college.college_email)
                try:
                    send_mail(subject, message, email, to_email)
                except BadHeaderError:
                    template = 'website/details.html'
                    context = {
                        'form': form,
                        'errors': 'Invalid header found.'
                    }
                    return render(request, template, context)
                return redirect('home')
            else:
                template = 'website/details.html'
                context = {
                    'form': form,
                    'errors': "This email doesnt belong to" + college.name
                }
                return render(request, template, context)
    template = 'website/details.html'
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, template, context)


def receive(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            college = College.objects.all().filter(name=form.cleaned_data.get('college_name'))[0]
            required_email_ext = college.college_ext
            email = form.cleaned_data.get('email')
            email_ext = email.split('@')[1]
            if required_email_ext == email_ext:
                subject = 'Subject'
                message = "Here's a form :" + college.form_receive
                to_email = list(college.college_email)
                try:
                    send_mail(subject, message, email, to_email)
                except BadHeaderError:
                    template = 'website/details.html'
                    context = {
                        'form': form,
                        'errors': 'Invalid header found.'
                    }
                    return render(request, template, context)
                return redirect('home')

    template = 'website/details.html'
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, template, context)
