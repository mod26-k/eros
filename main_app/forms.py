from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile

class ProfileCreationForm(UserCreationForm, ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'