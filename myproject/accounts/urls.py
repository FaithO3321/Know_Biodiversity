from django.urls import path
from accounts.views import CustomLoginView, CustomRegisterView


urlpatterns = [
    path(
        'auth/login/',
        CustomLoginView.as_view(),
        name='custom_login'
    ),
    path(
        'auth/registration/',
        CustomRegisterView.as_view(),
        name='custom_registration'
        ),
]
