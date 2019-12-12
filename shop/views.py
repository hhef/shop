from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login


def home_page(request):
    return render(request, 'home_page.html')


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        pass
    return render(request, "contact/contact.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/login")
    return render(request, "auth/login.html", context)
