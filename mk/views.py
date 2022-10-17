from django.shortcuts import render

# Create your views here.
def mk(request):
    return render(request, 'mk.html')