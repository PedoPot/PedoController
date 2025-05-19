from django.db import models

class SocialNetwork(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    token           = models.CharField(max_length=255)
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_token(self):
        return self.token