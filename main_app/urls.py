from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    path('home/', views.home, name='home'),
    path('users/', views.users, name='users_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

    path('date-ideas/', views.DateIdeaList.as_view(), name='dateideas_list'),
    path('date-ideas/<int:dateidea_id>', views.dateideas_detail, name='dateidea_detail'),
    path('add-date-idea/', views.DateIdeaCreate.as_view(), name='dateidea_form'),

    # path('accounts/signup/', views.Signup.as_view(), name='signup'),
   
    path('accounts/signup/', views.signup, name='signup'),
    path('create-profile/', views.create_profile, name='create_profile')
]


