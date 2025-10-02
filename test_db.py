import os
import django
from django.conf import settings

# Configure Django settings
if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'neondb',
                'USER': 'neondb_owner',
                'PASSWORD': 'npg_AyoMDt4NX2QZ',
                'HOST': 'ep-rough-union-addgw2nk-pooler.c-2.us-east-1.aws.neon.tech',
                'PORT': '5432',
                'OPTIONS': {
                    'sslmode': 'require',
                },
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
        ],
    )

django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        print(f"Database connection successful: {result}")
except Exception as e:
    print(f"Database connection failed: {e}")
