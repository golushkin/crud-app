from django.views.generic.edit import CreateView
from .forms import CutomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CutomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
