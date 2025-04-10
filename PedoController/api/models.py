from django.db import models

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

class Api(models.Model):
    id              = models.AutoField(primary_key=True)
    socialNetwork   = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    token           = models.CharField(max_length=255)
    
    def __str__(self):
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.name + " - " + socialNetwork.name
    
    def get_id(self):
        return self.id
    
    def get_social_network(self):
        return self.socialNetwork
    
    def get_name(self):
        return self.name
    
    def get_token(self):
        return self.token

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
        socialNetwork = SocialNetwork.objects.get(id=self.socialNetwork.id)
        return self.username + " - " + self.fullName + " - " + socialNetwork.name

class SocialNetwork(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

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