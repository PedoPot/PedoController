from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Baiter as BaiterModel
from api.serializers import *
from django.shortcuts import render
import requests

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
        baiter = BaiterModel.objects.get(id=request.data['id'])
    except BaiterModel.DoesNotExist:
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
        baiter = BaiterModel.objects.get(id=id)
    except BaiterModel.DoesNotExist:
        return Response({'error': 'Baiter not found'}, status=404)
    baiter.delete()
    return Response({'message': 'Baiter deleted successfully'}, status=204)

"""
Function: find_one_baiter
Description: Get one Baiter with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Baiter.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_baiter(request):
    try:
        id = request.GET.get('id')
        baiter = BaiterModel.objects.get(id=id)
    except BaiterModel.DoesNotExist:
        return Response({'error': 'Baiter not found'}, status=404)
    serializer = BaiterSerializer(baiter)
    return Response(serializer.data)

"""
Function: find_all_baiters
Description: Get all Baiters.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_baiters(request):
    baiters = BaiterModel.objects.all()
    serializer = BaiterSerializer(baiters, many=True)
    return Response(serializer.data)

"""
Function: find_by_baiters
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
def find_by_baiters(request):
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
    
    baiters = BaiterModel.objects.filter(**filters)
    serializer = BaiterSerializer(baiters, many=True)
    return Response(serializer.data)