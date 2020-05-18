from django.shortcuts import render

# Create your views here.
def home(request):
    # home.html을 랜더링해오겠다.
    return render(request, 'home.html')

def close_finder(request):
    return render(request, 'CloseFinder/main.html')
