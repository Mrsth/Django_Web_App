from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import RegistrationForm

# Create your views here.
def user_creations(request):
    if request.method == "POST":
        signup_form = RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            messages.success(request,f"{username} Account created")
            return redirect('/blog')    
    else:    
        signup_form = RegistrationForm()
    return render(request, 'Signup.html', {"signup_form":signup_form})
