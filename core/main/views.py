from django.shortcuts import render


# Create your views here.
def MainView(request):
    return render(request, 'index.html')