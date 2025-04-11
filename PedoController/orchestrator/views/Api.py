from rest_framework.decorators import api_view
from rest_framework.response import Response
from orchestrator.models import Api
from orchestrator.serializers import ApiSerializer
from django.shortcuts import render
import requests


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
    serializer = ApiSerializer(api, data=request.data)
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
Function: find_one_api
Description: Get one api with the id.
Method: GET
Parameters:
    - id (int): The unique identifier for the api.
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_one_api(request):
    try:
        id = request.GET.get('id')
        api = Api.objects.get(id=id)
    except Api.DoesNotExist:
        return Response({'error': 'api not found'}, status=404)
    serializer = ApiSerializer(api)
    return Response(serializer.data)

"""
Function: find_all_api
Description: Get all api.
Method: GET
Parameters:
Returns:
    - Response : Data
"""
@api_view(['GET'])
def find_all_apis(request):
    apis = Api.objects.all()
    serializer = ApiSerializer(apis, many=True)
    return Response(serializer.data)

"""
Function: find_by_apis
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
def find_by_apis(request):
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

@api_view(['GET'])
def api_start(request):
    apis = Api.objects.all()
    url = "http://127.0.0.1:9341/pedoconnector/connector/start"
    headers = {
        "Content-Type": "application/json",
    }
    for api in apis:
        payload = {
            "connector": api.name,
            "token": api.token
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"error request: {e}")