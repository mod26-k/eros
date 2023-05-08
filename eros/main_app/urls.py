from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    # path('home/', views.home, name='home'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('date-ideas/', views.date_ideas, name='date_ideas_index'),
    # path('date-ideas/<int:pk>/', views.DateIdea.as_view() name='date_ideas_details'),
]
