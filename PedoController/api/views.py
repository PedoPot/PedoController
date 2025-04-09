from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import render

#%% # Pedophile Views

"""
Function: create_pedophile
Description: Creates a new Pedophile object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - nickname (str): The nickname of the Pedophile.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - score (int, optional): The score of pedophilia
Returns:
    - Response : Data
"""
@api_view(['POST'])
def create_pedophile(request):
    serializer = PedophileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


"""
Function: update_pedophile
Description: Update Pedophile object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Pedophile.
        - nickname (str): The nickname of the Pedophile.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - score (int, optional): The score of pedophilia
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_pedophile(request):
    try:
        pedophile = Pedophile.objects.get(id=request.data['id'])
    except Pedophile.DoesNotExist:
        return Response({'error': 'Pedophile not found'}, status=404)
    serializer = PedophileSerializer(pedophile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_pedophile
Description: Delete Pedophile with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the Pedophile.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_pedophile(id):
    try:
        pedophile = Pedophile.objects.get(id=id)
    except Pedophile.DoesNotExist:
        return Response({'error': 'Pedophile not found'}, status=404)
    pedophile.delete()
    return Response({'message': 'Pedophile deleted successfully'}, status=204)


"""
Function: get_pedophile
Description: Get one pedophile with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Pedophile.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_pedophile(request):
    try:
        id = request.GET.get('id')
        pedophile = Pedophile.objects.get(id=id)
    except Pedophile.DoesNotExist:
        return Response({'error': 'Pedophile not found'}, status=404)
    serializer = PedophileSerializer(pedophile)
    return Response(serializer.data)

"""
Function: list_pedophiles
Description: Get all pedophiles.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_pedophiles(request):
    pedophiles = Pedophile.objects.all()
    serializer = PedophileSerializer(pedophiles, many=True)
    return Response(serializer.data)


"""
Function: list_some_pedophiles
Description: Get some pedophiles based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Pedophile.
        - nickname (str): The nickname of the Pedophile.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - score (int, optional): The score of pedophilia
        - score_min : 10
        - score_max : 50
        - score_range : "10,50"
Returns:
    - Response : Data
"""
@api_view(['POST'])
def list_some_pedophiles(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'nickname' in request.data:
        filters['nickname'] = request.data['nickname']
    if 'score' in request.data:
        filters['score'] = request.data['score']
    if 'score_min' in request.data:
        filters['score__gte'] = request.data['score_min']
    if 'score_max' in request.data:
        filters['score__lte'] = request.data['score_max']
    if 'score_range' in request.data:
        try:
            score_min, score_max = map(int, request.data['score_range'].split(','))
            filters['score__gte'] = score_min
            filters['score__lte'] = score_max
        except ValueError:
            return Response({'error': 'Invalid score_range format. Use "min,max".'}, status=400)
    if 'socialNetwork' in request.data:
        filters['socialNetwork'] = request.data['socialNetwork']
    
    pedophiles = Pedophile.objects.filter(**filters)
    serializer = PedophileSerializer(pedophiles, many=True)
    return Response(serializer.data)

#%% # Api Views

"""
Function: create_api
Description: Creates a new Api object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - name (str): Api's name.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - token (int): token of api
Returns:
    - Response : Data
"""
@api_view(['POST'])
def create_api(request):
    serializer = ApiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
Function: update_api
Description: Update api object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the api.
        - name (str): Api's name.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - token (int, optional): token of api
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_api(request):
    try:
        api = Api.objects.get(id=request.data['id'])
    except Api.DoesNotExist:
        return Response({'error': 'api not found'}, status=404)
    serializer = PedophileSerializer(api, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_api
Description: Delete api with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the api.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_api(id):
    try:
        api = Api.objects.get(id=id)
    except Api.DoesNotExist:
        return Response({'error': 'Api not found'}, status=404)
    api.delete()
    return Response({'message': 'Api deleted successfully'}, status=204)


"""
Function: get_api
Description: Get one api with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the api.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_api(request):
    try:
        id = request.GET.get('id')
        api = Api.objects.get(id=id)
    except Api.DoesNotExist:
        return Response({'error': 'api not found'}, status=404)
    serializer = ApiSerializer(api)
    return Response(serializer.data)

"""
Function: list_api
Description: Get all api.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_api(request):
    api = Api.objects.all()
    serializer = ApiSerializer(api, many=True)
    return Response(serializer.data)

"""
Function: list_some_apis
Description: Get some api based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the api.
        - name (str): api's name.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - token (int): tokebn of api
Returns:
    - Response : Data
"""
@api_view(['POST'])
def list_some_apis(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'name' in request.data:
        filters['name'] = request.data['name']
    if 'socialNetwork' in request.data:
        filters['socialNetwork'] = request.data['socialNetwork']
    
    apis = Api.objects.filter(**filters)
    serializer = ApiSerializer(apis, many=True)
    return Response(serializer.data)


#%% # Baiter Views

"""
Function: create_baiter
Description: Creates a new Baiter object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - username (str): The username of the Baiter.
        - fullName (str): The full name of the Baiter.
        - email (str): The email of the Baiter.
        - password (str): The password of the Baiter.
        - bio (str): The bio of the Baiter.
        - location (str): The location of the Baiter.
        - gender (str): The gender of the Baiter.
        - birthDate (datetime): The date associated with the Baiter.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def create_baiter(request):
    serializer = BaiterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
Function: update_baiter
Description: Update Baiter object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Baiter.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - username (str): The username of the Baiter.
        - fullName (str): The full name of the Baiter.
        - email (str): The email of the Baiter.
        - password (str): The password of the Baiter.
        - bio (str): The bio of the Baiter.
        - location (str): The location of the Baiter.
        - gender (str): The gender of the Baiter.
        - birthDate (datetime): The date associated with the Baiter.
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_baiter(request):
    try:
        baiter = Baiter.objects.get(id=request.data['id'])
    except Baiter.DoesNotExist:
        return Response({'error': 'Baiter not found'}, status=404)
    serializer = BaiterSerializer(baiter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_baiter
Description: Delete Baiter with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the Baiter.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_baiter(request):
    try:
        id = request.GET.get('id')
        baiter = Baiter.objects.get(id=id)
    except Baiter.DoesNotExist:
        return Response({'error': 'Baiter not found'}, status=404)
    baiter.delete()
    return Response({'message': 'Baiter deleted successfully'}, status=204)

"""
Function: get_baiter
Description: Get one Baiter with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Baiter.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_baiter(request):
    try:
        id = request.GET.get('id')
        baiter = Baiter.objects.get(id=id)
    except Baiter.DoesNotExist:
        return Response({'error': 'Baiter not found'}, status=404)
    serializer = BaiterSerializer(baiter)
    return Response(serializer.data)

"""
Function: list_baiters
Description: Get all Baiters.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_baiters(request):
    baiters = Baiter.objects.all()
    serializer = BaiterSerializer(baiters, many=True)
    return Response(serializer.data)

"""
Function: list_some_baiters
Description: Get some Baiters based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Baiter.
        - username (str): The username of the Baiter.
        - email (str): The email of the Baiter.
        - location (str): The location of the Baiter.
        - gender (str): The gender of the Baiter.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def list_some_baiters(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'username' in request.data:
        filters['username'] = request.data['username']
    if 'email' in request.data:
        filters['email'] = request.data['email']
    if 'location' in request.data:
        filters['location'] = request.data['location']
    if 'gender' in request.data:
        filters['gender'] = request.data['gender']
    
    baiters = Baiter.objects.filter(**filters)
    serializer = BaiterSerializer(baiters, many=True)
    return Response(serializer.data)

#%% # SocialNetwork Views

"""
Function: create_social_network
Description: Creates a new SocialNetwork object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - name (str): The name of the SocialNetwork.
Returns:
    - Response : Data
"""

@api_view(['POST'])
def create_social_network(request):
    serializer = SocialNetworkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
Function: update_social_network
Description: Update SocialNetwork object based on the provided data.
Method: PUT
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the SocialNetwork.
        - name (str): The name of the SocialNetwork.
Returns:
    - Response : Data
"""
@api_view(['PUT'])
def update_social_network(request):
    try:
        social_network = SocialNetwork.objects.get(id=request.data['id'])
    except SocialNetwork.DoesNotExist:
        return Response({'error': 'SocialNetwork not found'}, status=404)
    serializer = SocialNetworkSerializer(social_network, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

"""
Function: delete_social_network
Description: Delete SocialNetwork with the id.
Method: DELETE
Parameters:
    - id (int): The unique identifier for the SocialNetwork.
Returns:
    - Response code 204 if successful, 404 if not found.
"""
@api_view(['DELETE'])
def delete_social_network(request):
    try:
        id = request.GET.get('id')
        social_network = SocialNetwork.objects.get(id=id)
    except SocialNetwork.DoesNotExist:
        return Response({'error': 'SocialNetwork not found'}, status=404)
    social_network.delete()
    return Response({'message': 'SocialNetwork deleted successfully'}, status=204)

"""
Function: get_social_network
Description: Get one SocialNetwork with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the SocialNetwork.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_social_network(request):
    try:
        id = request.GET.get('id')
        social_network = SocialNetwork.objects.get(id=id)
    except SocialNetwork.DoesNotExist:
        return Response({'error': 'SocialNetwork not found'}, status=404)
    serializer = SocialNetworkSerializer(social_network)
    return Response(serializer.data)

"""
Function: list_social_networks
Description: Get all SocialNetworks.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_social_networks(request):
    social_networks = SocialNetwork.objects.all()
    serializer = SocialNetworkSerializer(social_networks, many=True)
    return Response(serializer.data)

"""
Function: list_some_social_networks
Description: Get some SocialNetworks based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the SocialNetwork.
        - name (str): The name of the SocialNetwork.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def list_some_social_networks(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'name' in request.data:
        filters['name'] = request.data['name']
    
    social_networks = SocialNetwork.objects.filter(**filters)
    serializer = SocialNetworkSerializer(social_networks, many=True)
    return Response(serializer.data)

#%% # Message Views

"""
Function: create_message
Description: Creates a new Message object based on the provided data.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - conversation (int): The ID of the associated Conversation.
        - message (str): The content of the Message.
        - date (datetime): The date of the Message.
Returns:
    - Response : Data
"""
@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

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
Function: get_message
Description: Get one Message with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Message.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_message(request):
    try:
        id = request.GET.get('id')
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        return Response({'error': 'Message not found'}, status=404)
    serializer = MessageSerializer(message)
    return Response(serializer.data)

"""
Function: list_messages
Description: Get all Messages.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

"""
Function: list_some_messages
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
def list_some_messages(request):
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



#%% # Conversation Views

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
        conversation = Conversation.objects.get(id=request.data['id'])
    except Conversation.DoesNotExist:
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
        conversation = Conversation.objects.get(id=id)
    except Conversation.DoesNotExist:
        return Response({'error': 'conversation not found'}, status=404)
    conversation.delete()
    return Response({'message': 'conversation deleted successfully'}, status=204)

"""
Function: get_conversation
Description: Get one Conversation with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Conversation.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def get_conversation(request):
    try:
        id = request.GET.get('id')
        conversation = Conversation.objects.get(id=id)
    except Conversation.DoesNotExist:
        return Response({'error': 'Conversation not found'}, status=404)
    serializer = MessageSerializer(conversation)
    return Response(serializer.data)

"""
Function: list_conversations
Description: Get all Conversations.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def list_conversations(request):
    conversation = Conversation.objects.all()
    serializer = ConversationSerializer(conversation, many=True)
    return Response(serializer.data)

"""
Function: list_some_conversations
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
def list_some_conversations(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'baiter' in request.data:
        filters['baiter'] = request.data['baiter']
    if 'pedophile' in request.data:
        filters['pedophile'] = request.data['pedophile']
    
    messages = Conversation.objects.filter(**filters)
    serializer = ConversationSerializer(messages, many=True)
    return Response(serializer.data)
