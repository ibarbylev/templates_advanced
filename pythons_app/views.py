from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView

from pythons_core.decorators import group_required
from pythons_core.view_mixins import GroupRequiredMixin
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


# @group_required(groups=['User'])
# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#         print(form)
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')


@method_decorator(group_required(groups=['User']), name='dispatch')
class PythonCreateView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    form_class = PythonCreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
