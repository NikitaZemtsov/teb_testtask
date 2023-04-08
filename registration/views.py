from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginUserForm


def registration(request):
    return render(request, 'registration/register.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('user_profile')

def logout_user(requests):
    logout(requests)
    return redirect('login')

def user_profile(request):
    user = request.user
    content = {'user': user}
    return render(request, 'profile/profile.html', content)
