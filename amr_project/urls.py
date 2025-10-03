from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def home_view(request):
    return HttpResponse('''
    <h1>AMR App Backend</h1>
    <p>Backend is running successfully!</p>
    <ul>
        <li><a href="/admin/">Admin Panel</a></li>
        <li><a href="/api/">API Endpoints</a></li>
        <li><a href="/reset-password/">Reset Admin Password (Use once then remove!)</a></li>
    </ul>
    ''')

def reset_admin_password(request):
    User = get_user_model()
    try:
        admin_user = User.objects.get(username='admin')
        new_password = 'admin123'
        admin_user.set_password(new_password)
        admin_user.save()
        return HttpResponse(f'''
        <h1>Password Reset</h1>
        <p>Admin password has been reset to: <strong>{new_password}</strong></p>
        <p><a href="/admin/">Go to Admin Panel</a></p>
        <p><strong>IMPORTANT:</strong> Remove this reset endpoint after use for security!</p>
        ''')
    except User.DoesNotExist:
        new_password = 'admin123'
        User.objects.create_superuser('admin', 'robotzulurain@gmail.com', new_password)
        return HttpResponse(f'''
        <h1>Admin User Created</h1>
        <p>Admin user created with password: <strong>{new_password}</strong></p>
        <p><a href="/admin/">Go to Admin Panel</a></p>
        ''')

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('reset-password/', reset_admin_password),
    path('api/', include('amr_reports.urls')),
]
