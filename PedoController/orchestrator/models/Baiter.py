from django.db import models
from . import SocialNetwork

class Baiter(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    username        = models.CharField(max_length=255)
    fullName        = models.CharField(max_length=255)
    email           = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)
    bio             = models.CharField(max_length=255)
    location        = models.CharField(max_length=255)
    birthDate       = models.DateTimeField()
    
    GENDER_CHOICES = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
    ]
    
    gender     = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    def get_id(self):
        return self.id
    
    def get_social_network(self):
        return self.socialNetwork
    
    def get_username(self):
        return self.username
    
    def get_full_name(self):
        return self.fullName
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_bio(self):
        return self.bio
    
    def get_location(self):
        return self.location
    
    def get_birth_date(self):
        return self.birthDate
    
    def get_gender(self):
        return self.gender
    
    def __str__(self):
        return self.username + " - " + self.fullName + " - " + self.socialNetwork.name