import requests
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from urllib.parse import urlencode
from .serializers import UserSerializer
from .models import User

@api_view(['GET'])
def google_login_url(request):
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth"

    params = {
        'client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
        'redirect_uri': settings.GOOGLE_CALLBACK_URL,
        'response_type': 'code',
        'scope': 'email profile',
    }
    url = f"{google_auth_url}?{urlencode(params)}"

    return Response({"login_url": url})

@api_view(['GET'])
def google_callback(request):
    error = request.GET.get('error')
    if error:
        return Response({'error': error})

    code = request.GET.get('code')
    if not code:
        return Response({'error': 'Missing authorization code.'})

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'code': code,
        'client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_CALLBACK_URL,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()

    if 'error' in token_json:
        return Response({'error': token_json['error_description']})

    access_token = token_json.get('access_token')

    if not access_token:
        return Response({'error': 'Missing access token.'})

    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    user_info_params = {
        'access_token': access_token,
    }
    
    user_info_response = requests.get(user_info_url, params=user_info_params)
    user_info = user_info_response.json()

    if 'error' in user_info:
        return Response({'error': 'Failed to retrieve user info.'})

    # You can now use the user info (such as their email, name) for your app logic
    return Response({'success': True, 'user_info': user_info})

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                pass
                print(e)
                return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
