from .forms import CutomUserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_class = CutomUserCreationForm

    def form_invalid(self,form):
        json_errors = form.errors.get_json_data()
        for error_f in json_errors:
            for error_n in json_errors[error_f]:
                messages.error(self.request,'Error: {}'.format(error_n['message']))
        form.errors.clear()
        return super().form_invalid(form)

    def form_valid(self,form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
