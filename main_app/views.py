from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, DateIdeas, User, Pfp, PotentialMatch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
import os


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


# homepage / self
@login_required
def home(request):
    potential_matches = PotentialMatch.objects.filter(user=request.user)
    context = {'potential_matches': potential_matches}
    return render(request, 'main_app/home.html', context)



@login_required
def add_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Pfp.objects.create(url = url, user_id = user_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('home')

class UserUpdate(LoginRequiredMixin, UpdateView):
   model = Profile
   template_name = 'update_profile.html'
   fields = '__all__'

   def get_object(self, queryset = None):
      return self.request.user.profile

class UserDelete(LoginRequiredMixin, DeleteView):
   model = User
   template_name = 'main_app/user_confirm_delete.html'
   success_url = '/accounts/signup/'

   def get_object(self, queryset = None):
    return self.request.user

# Users
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

# "likes" or potential matches
def add_to_matches(request, pk):
   match_profile= get_object_or_404(Profile, pk=pk)
   PotentialMatch.objects.create(user = request.user, potential_match = match_profile.user)
   return render(request, 'main_app/home.html')

# def view_potential_matches(request):
#     potentialmatches = PotentialMatch.objects.all()
#     return render(request, 'main_app/home.html', {'potentialmatches': potentialmatches})

#Date ideas list and details
class DateIdeaList(LoginRequiredMixin, ListView):
   model = DateIdeas

def dateideas_detail(request, dateidea_id):
   dateidea = DateIdeas.objects.get(id=dateidea_id)
   return render(request, 'main_app/dateideas_detail.html', {'dateidea': dateidea})

class DateIdeaCreate(LoginRequiredMixin, CreateView):
   model = DateIdeas
   fields = ['restaurant', 'city', 'state', 'meal', 'date']
   success_url = reverse_lazy('dateideas_list')
   template_name = 'main_app/dateideas_form.html'

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
   def get_success_url(self):
      return reverse_lazy('dateideas_list')

class DateIdeaUpdate(LoginRequiredMixin, UpdateView):
   model = DateIdeas
   fields = ['restaurant', 'city', 'state', 'meal', 'date']

class DateIdeaDelete(LoginRequiredMixin, DeleteView):
   model = DateIdeas
   template_name = 'main_app/dateideas_confirm_delete.html'
   success_url = '/date-ideas'