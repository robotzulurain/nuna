import re

NETLIFY_URL = "https://nuna1.netlify.app"

with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Update CORS_ALLOWED_ORIGINS
if NETLIFY_URL not in content:
    # Replace the entire CORS_ALLOWED_ORIGINS list
    content = re.sub(
        r'CORS_ALLOWED_ORIGINS\s*=\s*\[[^\]]+\]',
        f'CORS_ALLOWED_ORIGINS = [\n    "http://localhost:5173",\n    "http://127.0.0.1:5173",\n    "http://localhost:3000",\n    "http://127.0.0.1:3000",\n    "{NETLIFY_URL}",\n]',
        content
    )
    
    # Update CSRF_TRUSTED_ORIGINS
    content = re.sub(
        r'CSRF_TRUSTED_ORIGINS\s*=\s*\[[^\]]+\]',
        f'CSRF_TRUSTED_ORIGINS = [\n    "http://localhost:5173",\n    "http://127.0.0.1:5173",\n    "{NETLIFY_URL}",\n]',
        content
    )

with open('amr_project/settings.py', 'w') as f:
    f.write(content)

print("CORS settings updated for Netlify!")
