from django.db import models

class Pedophile(models.Model):
    id                      = models.AutoField(primary_key=True)
    user_socialNetwork_id   = models.CharField(max_length=255, null=True)
    nickname                = models.CharField(max_length=255)
    score                   = models.IntegerField()
    socialNetwork           = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nickname + " - " + self.socialNetwork.name
    
    def get_score(self):
        return self.score
    
    def get_nickname(self):
        return self.nickname
    
    def get_social_network(self):
        return self.socialNetwork
    
    def get_id(self):
        return self.id
    
    def get_user_socialNetwork_id(self):
        return self.user_socialNetwork_id