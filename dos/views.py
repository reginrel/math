from django.shortcuts import render

# Create your views here.
def dos(request):
    return render(request, 'dos.html')