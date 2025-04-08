from django.db import models

class Pedophile(models.Model):
    id              = models.AutoField(primary_key=True)
    nickname        = models.CharField(max_length=255)
    score           = models.IntegerField()
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)

class Api(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    token           = models.CharField(max_length=255)

class Baiter(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    username        = models.CharField(max_length=255)
    fullName        = models.CharField(max_length=255)
    email           = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)
    bio             = models.CharField(max_length=255)
    location        = models.CharField(max_length=255)
    gender          = models.CharField(max_length=255)
    date            = models.DateTimeField()

class SocialNetwork(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)

class Conversation(models.Model):
    id              = models.AutoField(primary_key=True)
    Baiter          = models.ForeignKey('Baiter', on_delete=models.CASCADE)
    Pedophile       = models.ForeignKey('Pedophile', on_delete=models.CASCADE)

class Message(models.Model):
    id              = models.AutoField(primary_key=True)
    converation     = models.ForeignKey('conversation', on_delete=models.CASCADE)
    message         = models.CharField(max_length=255)
    date            = models.DateTimeField()