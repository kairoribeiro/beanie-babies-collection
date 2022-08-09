from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Baby


# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def babies_index(request):
    babies = Baby.objects.filter(user=request.user)
    return render(request, 'babies/index.html', { 'babies': babies })

@login_required
def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  return render(request, 'babies/detail.html', { 'baby': baby })

class BabyCreate(LoginRequiredMixin, CreateView):
  model = Baby
  fields = ['name', 'year', 'image', 'description']
  success_url = '/babies/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BabyUpdate(LoginRequiredMixin, UpdateView):
  model = Baby
  fields = ['year', 'image', 'description']

class BabyDelete(LoginRequiredMixin, DeleteView):
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


