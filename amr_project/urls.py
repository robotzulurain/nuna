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
    </ul>
    ''')

def reset_admin_password(request):
    User = get_user_model()
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('newpassword123')
        admin_user.save()
        return HttpResponse('Admin password has been reset to: <strong>newpassword123</strong><br><a href="/admin/">Go to Admin</a>')
    except User.DoesNotExist:
        User.objects.create_superuser('admin', 'robotzulurain@gmail.com', 'newpassword123')
        return HttpResponse('Admin user created with password: <strong>newpassword123</strong><br><a href="/admin/">Go to Admin</a>')

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('reset-password/', reset_admin_password),  # Remove this after use!
    path('api/', include('amr_reports.urls')),
]
