from django.db import models
from datetime import date
from . import SocialNetwork

class Baiter(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE, null=True)
    username        = models.CharField(max_length=255)
    fullName        = models.CharField(max_length=255)
    email           = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)
    bio             = models.CharField(max_length=255)
    location        = models.CharField(max_length=255)
    birthDate       = models.DateTimeField()
    context         = models.CharField(max_length=1000, null=True)
    
    GENDER_CHOICES = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
    ]
    
    gender     = models.CharField(max_length=10, choices=GENDER_CHOICES)
    context    = models.CharField(max_length=1000, null=True)

    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_social_network(self):
        return self.socialNetwork
    
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

    def get_context(self):
        return self.context
    
    def __str__(self):
        return self.username + " - " + self.fullName + " - " + self.socialNetwork.name
    
    # context is the description of the baiter ex: Jean, enfant de 14 ans qui aime la musique et les tracteurs
    def set_context(self):
        self.context = f"{self.fullName}, child of {self.calculate_age()} years old who live in {self.location}. {self.fullName} descripe himself : {self.bio}"
        self.save()

    def calculate_age(self):
        today = date.today()
        return today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
    
    def get_context(self):
        return self.context
