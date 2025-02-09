import django
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_service.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

## superuser
users_data = [
    {"username": "admin", "email": "admin@email.com", "password": "admin123", "is_staff": True}
]

## users
for i in range(1, 11):
    users_data.append({
        "username": f"usuario{i}",
        "email": f"usuario{i}@email.com",
        "password": f"usuario-pass{i}"
    })

for user_data in users_data:
    user, created = User.objects.get_or_create(username=user_data["username"], defaults={
        "email": user_data["email"],
        "is_staff": user_data.get("is_staff", False)
    })

    if created:
        user.set_password(user_data["password"])
        user.save()
        token = Token.objects.create(user=user)
        print(f"Usuario {user.username} creado con Token: {token.key}")
    else:
        print(f"Usuario {user.username} ya existe")

print("Usuarios creados con éxito")