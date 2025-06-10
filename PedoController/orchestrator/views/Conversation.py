from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import Conversation as ConversationModel
from orchestrator.serializers import ConversationSerializer, MessageSerializer
from django.shortcuts import render
import requests
from orchestrator.views.Message import initFirstMessage


"""
Function: create_conversation
Description: Creates a new Conversation object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - Baiter (int): The ID of the associated baiter.
        - Pedophile (str): The ID of the associated pedo.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def create_conversation(request):
    serializer = ConversationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        try:
            print(initFirstMessage(
                serializer.data['id'],
                serializer.data['baiter']
            ))
        except Exception as e:
            print(f"Error initializing first message: {e}")
            
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
Function: update_conversation
Description: Update Conversation object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Conversation.
        - Baiter (int): The ID of the associated baiter.
        - Pedophile (str): The ID of the associated pedo.
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_conversation(request):
    try:
        conversation = ConversationModel.objects.get(id=request.data['id'])
    except ConversationModel.DoesNotExist:
        return Response({'error': 'Conversation not found'}, status=404)
    serializer =ConversationSerializer(conversation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_conversation
Description: Delete conversation with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the conversation.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_conversation(request):
    try:
        id = request.GET.get('id')
        conversation = ConversationModel.objects.get(id=id)
    except ConversationModel.DoesNotExist:
        return Response({'error': 'conversation not found'}, status=404)
    conversation.delete()
    return Response({'message': 'conversation deleted successfully'}, status=204)

"""
Function: find_one_conversation
Description: Get one Conversation with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Conversation.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_conversation(request):
    try:
        id = request.GET.get('id')
        conversation = ConversationModel.objects.get(id=id)
    except ConversationModel.DoesNotExist:
        return Response({'error': 'Conversation not found'}, status=404)
    serializer = MessageSerializer(conversation)
    return Response(serializer.data)

"""
Function: find_all_conversations
Description: Get all Conversations.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_conversations(request):
    conversation = ConversationModel.objects.all()
    serializer = ConversationSerializer(conversation, many=True)
    return Response(serializer.data)

"""
Function: find_by_conversations
Description: Get some conversation based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Conversation.
        - Baiter (int): The ID of the associated baiter.
        - Pedophile (str): The ID of the associated pedo.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def find_by_conversations(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'baiter' in request.data:
        filters['baiter'] = request.data['baiter']
    if 'pedophile' in request.data:
        filters['pedophile'] = request.data['pedophile']
    
    messages = ConversationModel.objects.filter(**filters)
    serializer = ConversationSerializer(messages, many=True)
    return Response(serializer.data)

def find_by_conversations_function(filters, order_by=None):
    conversations = ConversationModel.objects.filter(**filters)
    if order_by:
        conversations = conversations.order_by(order_by["name"])
        if order_by["sort"] == "DESC":
            conversations = conversations.reverse()
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_conversations(request):
    data = find_by_conversations(request)
    first = request.data['numberPage']-1* request.data['numberResults']
    last = request.data['numberPage'] * request.data['numberResults']
    data = data[first:last]
    return Response(data)