from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    path('home/', views.home, name='home'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('users/', views.users, name='users_index'),

    path('date-ideas/', views.DateIdeaList.as_view(), name='dateideas_list'),
    path('date-ideas/<int:dateidea_id>', views.dateideas_detail, name='dateidea_detail'),
    path('add-date-idea/', views.DateIdeaCreate.as_view(), name='dateidea_form'),
    # path('date-ideas/<int:pk>/', views.DateIdea.as_view(), name='date_ideas_details'),
    path('accounts/signup/', views.signup, name='signup'),

]


