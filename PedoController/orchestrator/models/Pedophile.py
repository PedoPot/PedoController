from django.db import models
from . import SocialNetwork

class Pedophile(models.Model):
    id              = models.AutoField(primary_key=True)
    nickname        = models.CharField(max_length=255)
    score           = models.IntegerField()
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.nickname + " - " + socialNetwork.name
    
    def get_score(self):
        return self.score
    
    def get_nickname(self):
        return self.nickname
    
    def get_social_network(self):
        return self.socialNetwork
    
    def get_id(self):
        return self.id