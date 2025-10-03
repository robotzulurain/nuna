from rest_framework.decorators import api_view
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
