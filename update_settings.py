import re

# Read the current settings
with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Add imports if not present
if 'import dj_database_url' not in content:
    # Add after existing imports
    import_match = re.search(r'(import os|from pathlib import Path)', content)
    if import_match:
        insert_pos = import_match.start()
        content = content[:insert_pos] + 'import os\nimport dj_database_url\n' + content[insert_pos:]

# Replace database configuration
new_db_config = '''
# Database configuration for Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_AyoMDt4NX2QZ@ep-rough-union-addgw2nk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
'''

# Find and replace existing DATABASES
if 'DATABASES' in content:
    # Replace existing DATABASES
    content = re.sub(r"DATABASES\s*=\s*\{[^}]+\}", new_db_config, content)
else:
    # Add DATABASES if not present
    content += '\n\n' + new_db_config

# Write updated content
with open('amr_project/settings.py', 'w') as f:
    f.write(content)

print("Settings updated successfully!")
