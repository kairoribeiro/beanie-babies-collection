from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Baby


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def babies_index(request):
    babies = Baby.objects.all()
    return render(request, 'babies/index.html', { 'babies': babies })

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  return render(request, 'babies/detail.html', { 'baby': baby })

class BabyCreate(CreateView):
  model = Baby
  fields = '__all__'
  success_url = '/babies/'

class BabyUpdate(UpdateView):
  model = Baby
  fields = ['year', 'image', 'description']

class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'


