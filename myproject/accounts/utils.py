from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed


def custom_exception_handler(exc, context):
    """
    Custom exception handler to provide user-friendly error
    messages for various types of exceptions.
    """

    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, AuthenticationFailed):
            response.data = {'detail': 'Invalid login. Please try again.'}
        else:
            response.data = {'detail': 'An error occurred. Please try again.'}

    return response
