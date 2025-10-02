import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')

try:
    django.setup()
except Exception as e:
    print(f"Django setup failed: {e}")
    sys.exit(1)

from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()

def main():
    # Get from environment variables
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'robotzulurain@gmail.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    
    if not password:
        print("ERROR: DJANGO_SUPERUSER_PASSWORD environment variable not set!")
        return
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return
    
    try:
        if User.objects.filter(username=username).exists():
            print(f"User '{username}' already exists")
            return
        
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully!")
        
    except Exception as e:
        print(f"Error creating superuser: {e}")

if __name__ == '__main__':
    main()
