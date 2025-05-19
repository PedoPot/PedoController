from django.db import models
from . import Baiter
from . import Pedophile

class Conversation(models.Model):
    id              = models.AutoField(primary_key=True)
    baiter          = models.ForeignKey('Baiter', on_delete=models.CASCADE)
    pedophile       = models.ForeignKey('Pedophile', on_delete=models.CASCADE)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.baiter.username} - {self.pedophile.nickname}"
    
    def get_id(self):
        return self.id
    
    def get_baiter(self):
        return self.baiter
    
    def get_pedophile(self):
        return self.pedophile
    
    def get_social_network(self):
        return self.socialNetwork