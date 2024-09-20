from django.shortcuts import render
from app.models import Summary
from django.db import connection

def index(request):
    summaries = Summary.objects.select_related(
        'school', 
        'student', 
        'subject', 
        'assessment_area', 
        'award'
    ).all()

    return render(request, 'index.html', {'summaries': summaries})


def visualize_tables(request):
    with connection.cursor() as cursor:
        # Get all table names from the SQLite database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

    table_data = {}
    
    for table in tables:
        table_name = table[0]
        with connection.cursor() as cursor:
            # Get column information for each table
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = [col[1] for col in cursor.fetchall()]  # col[1] is the column name
        table_data[table_name] = columns
    
    return render(request, 'visualize_tables.html', {'table_data': table_data})