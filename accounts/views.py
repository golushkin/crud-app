from .forms import CutomUserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = CutomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request,'You created an account')
            return redirect("home")
        else:
            for field in form:
                for msg in field.errors:
                    messages.error(request,'Error: {}'.format(msg))
    form = CutomUserCreationForm()
    return render(request = request,
                  template_name = "signup.html",
                  context={"form":form})