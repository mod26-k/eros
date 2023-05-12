from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    path('accounts/signup/', views.signup, name='signup'),
    path('create-profile/', views.create_profile, name='create_profile'),

    path('home/', views.home, name='home'),
    path('home/add_photo/<int:user_id>/', views.add_photo, name='add_photo'),

    path('users/', views.users, name='users_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),

    path('date-ideas/', views.DateIdeaList.as_view(), name='dateideas_list'),
    path('date-ideas/<int:dateidea_id>', views.dateideas_detail, name='dateidea_detail'),
    path('add-date-idea/', views.DateIdeaCreate.as_view(), name='dateidea_form'),
    path('date-ideas/<int:pk>/update/', views.DateIdeaUpdate.as_view(), name='dateideas_update'),
    path('date-ideas/<int:pk>/delete/', views.DateIdeaDelete.as_view(), name='dateideas_delete'),
]


