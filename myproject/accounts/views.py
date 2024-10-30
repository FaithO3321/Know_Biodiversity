from django.shortcuts import render
from dj_rest_auth.views import LoginView, RegisterView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed


class CustomLoginView(LoginView):
    """
    Custom login view that handles authentication errors and
    returns custom error messages for failed logins.
    """
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except AuthenticationFailed:
            return Response(
                {"detail": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST
            )


class CustomRegisterView(RegisterView):
    """
    Custom registration view that handles errors during
    the user registration process.
    """
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except Exception:
            return Response(
                {"detail": "User registration failed. Check your input."},
                status=status.HTTP_400_BAD_REQUEST
                )
