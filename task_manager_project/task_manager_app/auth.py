# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions


class CustomHeaderAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        username = request.META.get("HTTP_X_TELEGRAM")
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            # user.is_superuser = False
            # user.save()
            raise exceptions.AuthenticationFailed("No such user")

        return (user, None)
