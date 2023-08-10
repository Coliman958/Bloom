from django.urls import path
from members import views
from .views import DisplayProfileView, EditProfileView, CreateProfileView,UserRegistrationView, ProfileSettingsView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile_settings/', ProfileSettingsView.as_view(), name='edit_profile_setting'),
    path('members/password/', auth_views.PasswordChangeView.as_view()),     # url to manually change password
    path('<int:pk>/profile/', DisplayProfileView.as_view(), name='profile'),
    path('<int:pk>/edit_profile_page/', EditProfileView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),


]