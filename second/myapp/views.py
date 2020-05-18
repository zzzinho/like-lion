from django.shortcuts import render
from .models import Test

# Create your views here.
def index(request):
    try:
        temp_object = Test.objects.all()
        context = {'myobject': temp_object}
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')

def result(request):
    temp_target = request.GET['target']
    word_len = len(temp_target)
    context = {'display_value': word_len}

    return render(request, 'result.html', context)
    