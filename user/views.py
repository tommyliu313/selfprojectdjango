from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request, 'user/dashboard.html')

def login():
    pass

def logout():
    pass