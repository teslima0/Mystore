import email
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q

'''
class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, Password= None, **kwargs):
        UserModel= get_user_model()
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:

            return None
        else:
            if user.check_password(Password):
                return user
        return None
'''

class EmailBackEnd(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try: #to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None