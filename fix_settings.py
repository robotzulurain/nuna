# Read the original settings
with open('amr_project/settings.py', 'r') as f:
    lines = f.readlines()

# Find where to insert the production settings
# We'll add them after the existing DATABASES configuration
new_lines = []
database_found = False
database_replaced = False

for line in lines:
    if 'DATABASES = {' in line and not database_replaced:
        new_lines.append('''# Database configuration for Neon
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_AyoMDt4NX2QZ@ep-rough-union-addgw2nk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

''')
        database_replaced = True
        # Skip the existing database configuration
        continue
    elif database_replaced and line.strip().startswith('}'):
        # Skip the closing brace of old database config
        continue
    elif database_replaced and line.strip() == '':
        # Skip empty lines after database config
        continue
    else:
        new_lines.append(line)

# Write the updated settings
with open('amr_project/settings.py', 'w') as f:
    f.writelines(new_lines)

print("Settings updated successfully!")
