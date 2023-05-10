from django.shortcuts import render, redirect
from .models import Profile, DateIdeas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm
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
def users(request):
    all_users = Profile.objects.all()
    # all_users = User.objects.all()
    return render(request, 'main_app/users_list.html')

class DateIdeaList(LoginRequiredMixin, ListView):
   model = DateIdeas

def dateideas_detail(request, dateidea_id):
   dateidea = DateIdeas.objects.get(id=dateidea_id)
   return render(request, 'main_app/dateideas_detail.html', {'dateidea': dateidea})

class DateIdeaCreate(LoginRequiredMixin, CreateView):
   model = DateIdeas
   fields = '__all__'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('create_profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def create_profile(request):
    profile_form = UserCreationForm()
    if request.method == 'POST':
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        profile_form = UserCreationForm()
    # context = {'profile_form': profile_form}
    return render(request, 'create_profile.html', {'profile_form': profile_form})

class UserDetail(LoginRequiredMixin, DetailView):
   model = Profile
   template_name = 'user_detail.html'
