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
    serializer = MessageSerializer(data)

    if serializer.is_valid():
        serializer.save()
        url = "http://127.0.0.1:9341/pedoconnector/sendDirectMessage"
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            'connector': str,
            'token': str,
            'user_id': str,
            'message': str,
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"error request: {e}")
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_ai_message(request):
    data=request.data
    data['sender_type'] = 'assistant'
    create_message(data)

@api_view(['POST'])
def create_pedophile_message(request):
    data=request.data
    data['sender_type'] = 'user'
    create_message(data)

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
