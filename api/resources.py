# resources.py

from tastypie.resources import ModelResource
from api.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
