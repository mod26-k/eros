# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'dateideas')
