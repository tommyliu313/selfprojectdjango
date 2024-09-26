from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import User
from transfer.models import Transfer

# Create your views here.

# return to dashboard, show his information and record
def dashboard(request):
    user_info = get_object_or_404(User)
    return render(request, 'user/dashboard.html')


def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')

def register(request):
    return render(request, 'user/register.html')