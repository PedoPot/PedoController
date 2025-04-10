from rest_framework import serializers
from .models import *

class PedophileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedophile
        fields = '__all__'
        
class ApiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Api
        fields = '__all__'
        
class BaiterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Baiter
        fields = '__all__'
        
class SocialNetworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialNetwork
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Conversation
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'