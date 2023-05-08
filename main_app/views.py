from django.shortcuts import render, redirect
from .models import Profile, DateIdeas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

@login_required
def myprofile(request):
    return render(request, 'main_app/myprofile.html')

@login_required
def users(request):
    all_users = Profile.objects.all()
    # all_users = User.objects.all()
    return render(request, 'main_app/users_index.html')

# @login_required
# def date_ideas(request):
#     date_ideas = DateIdeas.objects.all()
#     return render(request, 'date_ideas/date_ideas_index.html', {
#     'date_ideas': date_ideas
#     })

class DateIdeaList(LoginRequiredMixin, ListView):
   model = DateIdeas

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)