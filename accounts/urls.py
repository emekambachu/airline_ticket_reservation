from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [

    # use the django login view and add the template you would be using for it

    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', views.UserSignUpPage.as_view(), name='signup'),

]