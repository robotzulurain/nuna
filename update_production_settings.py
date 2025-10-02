import os

settings_updates = '''
# ===== PRODUCTION SETTINGS - ADD TO YOUR settings.py =====

import os
import dj_database_url
from pathlib import Path

# Database configuration for Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_AyoMDt4NX2QZ@ep-rough-union-addgw2nk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings for production
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', '.netlify.app']

# Add whitenoise to middleware (add this after SecurityMiddleware)
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Add this line
#     # ... rest of your middleware
# ]

# If you have CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-netlify-app.netlify.app",
]

CORS_ALLOW_ALL_ORIGINS = True  # For development, restrict in production
'''

print("Add these settings to your amr_project/settings.py file")
print(settings_updates)
