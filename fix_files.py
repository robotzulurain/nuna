import os

# 1. Fix amr_reports/urls.py
urls_content = '''from django.urls import path
from . import api_real as api
from . import views  # Import the new views

urlpatterns = [
    # SUMMARY
    path('summary/counts-summary', api.CountsSummaryView.as_view()),
    path('summary/time-trends',    api.TimeTrendsView.as_view()),
    path('summary/antibiogram',    api.AntibiogramView.as_view()),
    path('summary/sex-age',        api.SexAgeView.as_view()),

    # GEO
    path('geo/facilities', api.FacilitiesView.as_view()),

    # OPTIONS / ENTRY / UPLOAD / TEMPLATE
    path('options',       api.OptionsView.as_view()),
    path('entry',         api.ManualEntryView.as_view()),
    path('upload',        api.UploadView.as_view()),
    path('upload/csv',    views.upload_csv, name='upload_csv'),  # ADDED THIS LINE
    path('templates/csv', api.TemplateCSVView.as_view()),

    # ALERTS / EXPORT
    path('alerts',        api.AlertsView.as_view()),
    path('export/glass',  api.GlassExportView.as_view()),

    # AUTH
    path('auth/token',  api.TokenView.as_view()),
    path('auth/whoami', api.WhoAmIView.as_view()),
]
'''

# 2. Fix amr_reports/views.py
views_content = '''from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import csv
import io

@api_view(['POST'])
def upload_csv(request):
    """
    Handle CSV file uploads
    """
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    csv_file = request.FILES['file']
    
    # Check if the file is a CSV
    if not csv_file.name.endswith('.csv'):
        return Response({'error': 'File is not a CSV'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Read and process the CSV file
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.reader(io_string)
        
        # Process the CSV data
        rows = list(reader)
        headers = rows[0] if rows else []
        data_rows = rows[1:] if len(rows) > 1 else []
        
        return Response({
            'message': 'CSV uploaded successfully',
            'headers': headers,
            'row_count': len(data_rows)
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
'''

# 3. Fix main urls.py
main_urls_content = '''from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('''
    <h1>AMR App Backend</h1>
    <p>Backend is running successfully!</p>
    <ul>
        <li><a href="/admin/">Admin Panel</a></li>
        <li><a href="/api/">API Endpoints</a></li>
    </ul>
    ''')

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('amr_reports.urls')),
]
'''

# Write the files
with open('amr_reports/urls.py', 'w') as f:
    f.write(urls_content)

with open('amr_reports/views.py', 'w') as f:
    f.write(views_content)

with open('amr_project/urls.py', 'w') as f:
    f.write(main_urls_content)

print("Backend files fixed successfully!")
