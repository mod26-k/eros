from django.shortcuts import render
from .models import Profile, DateIdeas

def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def myprofile(request):
    return render(request, 'user/myprofile.html')

def date_ideas(request):
    date_ideas = DateIdeas.objects.all()
    return render(request, 'date_ideas/date_ideas_index.html', {
    'date_ideas': date_ideas
    })