from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
     return Response({
        "message": "Hello from CSC 325 CI/CD!",
        "status": "CI/CD pipeline working!"
    })

# CI/CD pull request testgit add api/views.py