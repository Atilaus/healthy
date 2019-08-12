from django.urls import path
from .views import login_view


urlpatterns = [
	path('accounts/login/', login_view, name='login_url')
]