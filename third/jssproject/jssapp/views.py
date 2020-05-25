from django.shortcuts import render, redirect

from .models import Jasoseol
from .forms import JssForm

# Create your views here.
def index(request):
    try:
        jss = Jasoseol.objects.all()
        context = {'jss_obj': jss}
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        myform = JssForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('index')

    myform = JssForm()
    return render(request, 'create.html', {'myform':myform})

def detail(request, jss_id):
    my_jss = Jasoseol.objects.get(pk='jss_id')
    return render(request, 'detail.html', {'my_jss': my_jss})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.method == "POST":
        update_form = JssForm(request.POST, instance=my_jss)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
            
    update_form = JssForm(instance=my_jss)
    return render(request, 'update.html', {'update_form': update_form})
