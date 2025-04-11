from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import SocialNetwork
from orchestrator.serializers import SocialNetworkSerializer
from django.shortcuts import render
import requests

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
Function: find_one_social_network
Description: Get one SocialNetwork with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the SocialNetwork.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_social_network(request):
    try:
        id = request.GET.get('id')
        social_network = SocialNetwork.objects.get(id=id)
    except SocialNetwork.DoesNotExist:
        return Response({'error': 'SocialNetwork not found'}, status=404)
    serializer = SocialNetworkSerializer(social_network)
    return Response(serializer.data)

"""
Function: find_all_social_networks
Description: Get all SocialNetworks.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_social_networks(request):
    social_networks = SocialNetwork.objects.all()
    serializer = SocialNetworkSerializer(social_networks, many=True)
    return Response(serializer.data)

"""
Function: find_by_social_networks
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
def find_by_social_networks(request):
    filters = {}
    if 'id' in request.data:
        filters['id'] = request.data['id']
    if 'name' in request.data:
        filters['name'] = request.data['name']
    
    social_networks = SocialNetwork.objects.filter(**filters)
    serializer = SocialNetworkSerializer(social_networks, many=True)
    return Response(serializer.data)