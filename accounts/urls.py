from django.urls import path
from .views import login_view, register_view, logout_view


urlpatterns = [
	path('accounts/login/', login_view, name='login_url'),
	path('accounts/register/', register_view, name='register_url'),
	path('accounts/logout/',logout_view, name='logout_url') 
]