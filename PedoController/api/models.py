from django.db import models

class Pedophile(models.Model):
    id              = models.AutoField(primary_key=True)
    nickname        = models.CharField(max_length=255)
    score           = models.IntegerField()
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.nickname + " - " + socialNetwork.name

class Api(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    token           = models.CharField(max_length=255)
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.name + " - " + socialNetwork.name

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
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.username + " - " + self.fullName + " - " + socialNetwork.name

class SocialNetwork(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Conversation(models.Model):
    id              = models.AutoField(primary_key=True)
    baiter          = models.ForeignKey('Baiter', on_delete=models.CASCADE)
    pedophile       = models.ForeignKey('Pedophile', on_delete=models.CASCADE)
    
    def __str__(self):
        baiter = Baiter.objects.get(id=self.baiter.id)
        pedophile = Pedophile.objects.get(id=self.pedophile.id)
        return f"{baiter.username} - {pedophile.nickname}"

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