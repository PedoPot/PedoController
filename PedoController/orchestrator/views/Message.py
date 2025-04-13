from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import Message
from orchestrator.serializers import MessageSerializer
from django.shortcuts import render
import requests

"""
Function: create_message
Description: Creates a new Message object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - conversation (int): The ID of the associated Conversation.
        - message (str): The content of the Message.
        - date (datetime): The date of the Message.
        - sender_type (str): The type of sender (assistant, user, system).
Returns:
    - Response : Data
"""
def create_message(data):
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_ai_message(request):
    data = request.data.copy()
    data['sender_type'] = 'assistant'
    try:
        response = create_message(data)
        
        url = "http://127.0.0.1:9341/pedoconnector/sendDirectMessage"
        headers = {
            "Content-Type": "application/json",
        }
        
        message = Message.objects.get(id=response.data['id'])
        conversation = message.get_conversation()
        
        payload = {
            'connector': conversation.get_baiter().get_api().get_name(),
            'token': conversation.get_baiter().get_api().get_token(),
            'user_id': conversation.get_pedophile().get_user_socialNetwork_id(),
            'message': message.get_message(),
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    return Response({'message': 'Message created successfully'}, status=201)

@api_view(['POST'])
def create_pedophile_message(request):
    data=request.data
    data['sender_type'] = 'user'
    return create_message(data)

"""
Function: update_message
Description: Update Message object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Message.
        - conversation (int): The ID of the associated Conversation.
        - message (str): The content of the Message.
        - date (datetime): The date of the Message.
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_message(request):
    try:
        message = Message.objects.get(id=request.data['id'])
    except Message.DoesNotExist:
        return Response({'error': 'Message not found'}, status=404)
    serializer = MessageSerializer(message, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_message
Description: Delete Message with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the Message.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_message(request):
    try:
        id = request.GET.get('id')
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        return Response({'error': 'Message not found'}, status=404)
    message.delete()
    return Response({'message': 'Message deleted successfully'}, status=204)

"""
Function: find_one_message
Description: Get one Message with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Message.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_message(request):
    try:
        id = request.GET.get('id')
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        return Response({'error': 'Message not found'}, status=404)
    serializer = MessageSerializer(message)
    return Response(serializer.data)

"""
Function: find_all_messages
Description: Get all Messages.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

"""
Function: find_by_messages
Description: Get some Messages based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Message.
        - conversation (int): The ID of the associated Conversation.
        - date (datetime): The date of the Message.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def find_by_messages(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'conversation' in request.data:
        filters['conversation'] = request.data['conversation']
    if 'date' in request.data:
        filters['date'] = request.data['date']
    
    messages = Message.objects.filter(**filters)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
