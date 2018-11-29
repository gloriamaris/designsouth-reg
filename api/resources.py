# resources.py

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        fields = ['name', 'email', 'school']
