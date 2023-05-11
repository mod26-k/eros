from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, DateIdeas, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Views accessible to anyone
def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

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


# Views accessible to registered users
@login_required
def create_profile(request):
    profile_form = ProfileCreationForm()
    if request.method == 'POST':
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        profile_form = ProfileCreationForm()
    # context = {'profile_form': profile_form}
    return render(request, 'create_profile.html', {'profile_form': profile_form})


# User profile and other users list and details
@login_required
def home(request):
    return render(request, 'main_app/home.html')

@login_required
def users(request):
    # all_users = Profile.objects.all()
    all_users = User.objects.all()
    return render(request, 'main_app/users_list.html', {'all_users': all_users})

class UserDetail(LoginRequiredMixin, DetailView):
   model = Profile
   template_name = 'main_app/user_detail.html'

   def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user


#Date ideas list and details
class DateIdeaList(LoginRequiredMixin, ListView):
   model = DateIdeas

def dateideas_detail(request, dateidea_id):
   dateidea = DateIdeas.objects.get(id=dateidea_id)
   return render(request, 'main_app/dateideas_detail.html', {'dateidea': dateidea})

class DateIdeaCreate(LoginRequiredMixin, CreateView):
   model = DateIdeas
   fields = ['restaurant', 'city', 'state', 'meal', 'date']
#    success_url = reverse_lazy('date-ideas')
   template_name = 'main_app/dateideas_form.html'

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
