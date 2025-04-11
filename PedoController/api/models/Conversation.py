from django.db import models
from . import Baiter
from . import Pedophile

class Conversation(models.Model):
    id              = models.AutoField(primary_key=True)
    baiter          = models.ForeignKey('Baiter', on_delete=models.CASCADE)
    pedophile       = models.ForeignKey('Pedophile', on_delete=models.CASCADE)
    
    def __str__(self):
        baiter = Baiter.objects.get(id=self.baiter.id)
        pedophile = Pedophile.objects.get(id=self.pedophile.id)
        return f"{baiter.username} - {pedophile.nickname}"
    
    def get_id(self):
        return self.id
    
    def get_baiter(self):
        return self.baiter
    
    def get_pedophile(self):
        return self.pedophile