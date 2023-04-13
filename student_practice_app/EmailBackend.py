from django.contrib.auth import get_user_model # is fn,Return the User model that is active in this project.
from django.contrib.auth.backends import ModelBackend #is class,Authenticates against settings.AUTH_USER_MODEL.

class EmailBackend(ModelBackend):
 def authenticate(self,username=None, password=None, **kwargs):
    UserModel= get_user_model()
    try:
        user = UserModel.objects.get(email=username)
    except UserModel.DoesNotExist:
        return None
    else:
       if user.check_password(password):
          return user
    return None
           
    

