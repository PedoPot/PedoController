from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import Message
from orchestrator.models import Conversation
from orchestrator.serializers import MessageSerializer
from django.shortcuts import render
import requests
from orchestrator.models import Baiter


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
   
    data = request.POST.copy()
    data['sender_type'] = 'assistant'
    response = create_message(data)

    if response.status_code == 201:
        url = "http://pedo-connector:9341/sendDirectMessage"
        headers = {
            "Content-Type": "application/json",
        }
        
        conversation = Conversation.objects.get(id=response.data['conversation'])
        social_network = conversation.get_social_network()
        
        payload = {
            "connector": social_network.get_name(),
            "token": social_network.get_token(),
            "user_id": conversation.get_baiter().get_id(),
            "message": response.data['message'] 
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"error request: {e}")
    
    return response

@api_view(['POST'])
def create_pedophile_message(request):

    data = request.POST.copy()
    data['sender_type'] = 'user'
    
    response = create_message(data)
    if response.status_code == 201:
        url = "http://pedo-hunter-api:9344/chat"
        
        headers = {
            "Content-Type": "application/json",
        }
        filter = {}
        filter['conversation'] = response.data['conversation']
        items = find_by_messages_function(filter, order_by='date')
        payload = {
            "messages": [
                {
                    "role": item['sender_type'],
                    "content": item['message']
                }
                for item in items.data
            ]
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"error request: {e}")
            
    return response

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
    
    return find_by_messages_function(filters)

def find_by_messages_function(filters, order_by=None):
    messages = Message.objects.filter(**filters)
    if order_by:
        messages = messages.order_by(order_by)
    serializer = MessageSerializer(messages, many=True)
    print("serializer", serializer.data)
    return Response(serializer.data)

def initFirstMessage(idConversation, idBaiter):
    data = {}
    data['conversation'] = idConversation
    data['sender_type'] = 'system'
    data['date'] = '1970-01-01T00:00:00Z'
    data['message'] = Baiter.objects.get(id=idBaiter).get_context()
    return create_message(data)