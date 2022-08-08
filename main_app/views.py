from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Baby


# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

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
#   success_url = '/babies/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BabyUpdate(UpdateView):
  model = Baby
  fields = ['year', 'image', 'description']

class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('babies_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


