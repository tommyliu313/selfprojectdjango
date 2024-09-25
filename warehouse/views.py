from django.shortcuts import render, get_object_or_404

# Create your views here.

# show warehouse pages
# passing warehouse info
def warehouse(request):
    return render(request, 'warehouse/warehouse.html')

# show warehouse 



def order(request):
    pass