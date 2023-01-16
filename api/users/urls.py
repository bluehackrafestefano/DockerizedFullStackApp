from django.urls import path, include
from .views import RegistrationView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegistrationView.as_view()),
]
