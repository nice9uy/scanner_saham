from django.shortcuts import render
import yfinance as yf
from django.contrib import messages
from .models import DbAllStocks
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):

    return render(request, "home/index.html") 

def settings(request):
    return render(request, "home/settings.html")

def setting_data(request):
    try:
        stocks_settings = list(DbAllStocks.objects.values())
    except:
        pass
    return render(request, "parsial/all_stocks.html", {'stocks_settings': stocks_settings})


def upload_data_stocks(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        
        # Save the file temporarily
        fs = FileSystemStorage()
        file_path = fs.save(excel_file.name, excel_file)
        file_path = fs.path(file_path)

        # Read the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')

        # Iterate over the rows in the DataFrame and save them to the database
        for index, row in df.iterrows():
            DbAllStocks.objects.create(
                nip=row['NIP'],
                name=row['Name'],
                rank=row['Rank'],
                position=row['Position']
            )

        messages.success(request, "Data imported successfully!")
        return redirect('import_excel')

def get_data_yfinance(request):
    pass