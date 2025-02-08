import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

class RemoteTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        AUTH_SERVICE_URL = 'http://127.0.0.1:8000/validate_token/'

        try:
            response = requests.post(AUTH_SERVICE_URL, json={'token': key})
            if response.status_code == 200:
                user_data = response.json()

                user = get_user_model()
                user.id = user_data['id']
                user.username = user_data['username']
                user.email = user_data['email']
                user.is_staff = user_data['is_staff']
                user.is_authenticated = True
                return (user, key)
            
            raise AuthenticationFailed('Token invalido.')
        
        except requests.exceptions.ConnectionError:
            raise AuthenticationFailed('Error de conexión con el servicio de autenticación.')
        