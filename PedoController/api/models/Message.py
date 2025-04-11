from django.db import models

class Message(models.Model):
    id              = models.AutoField(primary_key=True)
    conversation     = models.ForeignKey('Conversation', on_delete=models.CASCADE)
    message         = models.CharField(max_length=255)
    date            = models.DateTimeField()
    
    SENDER_CHOICES = [
        ('assistant', 'Baiter'),
        ('user', 'Pedophile'),
        ('system', 'System'),
    ]
    
    sender_type     = models.CharField(max_length=10, choices=SENDER_CHOICES)
    
    def __str__(self):
        return f"{self.conversation} - {self.sender_type} - {self.date}"
    
    def get_id(self):
        return self.id
    
    def get_conversation(self):
        return self.conversation
    
    def get_message(self):
        return self.message
    
    def get_date(self):
        return self.date
    
    def get_sender_type(self):
        return self.sender_type