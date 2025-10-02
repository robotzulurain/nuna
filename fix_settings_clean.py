# Read the original settings
with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Remove any duplicate dj_database_url import if it exists
if content.count('import dj_database_url') > 1:
    content = content.replace('import dj_database_url\n', '', 1)

# Replace the entire DATABASES section with the correct one
new_db_config = '''# Database configuration for Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_AyoMDt4NX2QZ@ep-rough-union-addgw2nk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}'''

# Find and replace the DATABASES section
import re
content = re.sub(r'DATABASES\s*=\s*\{[^}]+\}', new_db_config, content)

# Remove any extra closing braces that might cause syntax errors
content = re.sub(r'\n\s*\n\s*\}', '\n', content)

# Write the fixed content back
with open('amr_project/settings.py', 'w') as f:
    f.write(content)

print("Settings cleaned successfully!")
