from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import Pedophile as PedophileModel
from orchestrator.serializers import PedophileSerializer
from django.shortcuts import render
import requests

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
        pedophile = PedophileModel.objects.get(id=request.data['id'])
    except PedophileModel.DoesNotExist:
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
        pedophile = PedophileModel.objects.get(id=id)
    except PedophileModel.DoesNotExist:
        return Response({'error': 'Pedophile not found'}, status=404)
    pedophile.delete()
    return Response({'message': 'Pedophile deleted successfully'}, status=204)


"""
Function: find_one_pedophile
Description: Get one pedophile with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the Pedophile.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_pedophile(request):
    try:
        id = request.GET.get('id')
        pedophile = PedophileModel.objects.get(id=id)
    except PedophileModel.DoesNotExist:
        return Response({'error': 'Pedophile not found'}, status=404)
    serializer = PedophileSerializer(pedophile)
    return Response(serializer.data)

"""
Function: find_all_pedophiles
Description: Get all pedophiles.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_pedophiles(request):
    pedophiles = PedophileModel.objects.all()
    serializer = PedophileSerializer(pedophiles, many=True)
    return Response(serializer.data)


"""
Function: find_by_pedophiles
Description: Get some pedophiles based on filters.
Method: POST
Parameters:
    - request (HttpRequest): The HTTP request containing the following data in the body:
        - id (int): The unique identifier for the Pedophile.
        - nickname (str): The nickname of the Pedophile.
        - socialNetwork (int): The ID of the associated SocialNetwork.
        - score (int, optional): The score of pedophilia
        - score__gte : 10
        - score__lte : 50
        - score_range : "10,50"
Returns:
    - Response : Data
"""
@api_view(['POST'])
def find_by_pedophiles(request):
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
    
    return  find_by_pedophiles_function(filters)

def find_by_pedophiles_function(filters, order_by=None):
    pedophiles = PedophileModel.objects.filter(**filters)
    if order_by:
        pedophiles = pedophiles.order_by(order_by["name"])
        if order_by["sort"] == "DESC":
            pedophiles = pedophiles.reverse()
    serializer = PedophileSerializer(pedophiles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_pedophiles(request):
    data = find_by_pedophiles(request)
    first = request.data['numberPage']-1* request.data['numberResults']
    last = request.data['numberPage'] * request.data['numberResults']
    data = data[first:last]
    return Response(data)