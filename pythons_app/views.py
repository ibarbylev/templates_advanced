from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from pythons_core.decorators import group_required
from .forms import PythonCreateForm
from .models import Python


# @login_required
# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})


# @login_required
class IndexListView(ListView):
    model = Python
    context_object_name = 'pythons'
    template_name = 'index.html'


@group_required(groups=['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
