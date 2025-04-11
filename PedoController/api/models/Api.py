from django.db import models
from . import SocialNetwork

class Api(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    token           = models.CharField(max_length=255)
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.name + " - " + socialNetwork.name
    
    def get_id(self):
        return self.id
    
    def get_social_network(self):
        return self.socialNetwork
    
    def get_name(self):
        return self.name
    
    def get_token(self):
        return self.token