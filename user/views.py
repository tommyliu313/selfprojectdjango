from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

# return to dashboard, show his information and record
@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')


def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')