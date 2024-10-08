from django.shortcuts import render
import yfinance as yf
from django.contrib import messages
from .models import DbAllStocks
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    stocks_jumlah = DbAllStocks.objects.count()

    context = {
        'stocks_jumlah' : stocks_jumlah
    }

    return render(request, "home/index.html", context) 

def settings(request):
    return render(request, "home/settings.html")

def setting_data(request):
    
    # Get all data from the model
    stocks = list(DbAllStocks.objects.all().order_by('id'))

    data = [
        {
            "id": item.id,
            "code": item.code,
            "company_name": item.company_name,
            "listing_board": item.listing_board,
        }
        for item in stocks
    ]

    return JsonResponse(data, safe=False)  
    

def upload_excel(request):
    if request.method == "POST":
        excel_file = request.FILES.get('file')

        print(excel_file)

        if not excel_file:
            messages.error(request, "Tidak ada file yang diunggah.")
            return redirect('settings')  # Ubah dengan view yang sesuai

        # Pastikan file memiliki format yang benar
        if not excel_file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Format file tidak didukung. Harus berupa file Excel.")
            return redirect('settings')

        # Membaca file Excel menggunakan Pandas
        try:
            df = pd.read_excel(excel_file, engine='openpyxl')  # Membaca file Excel
        except Exception as e:
            messages.error(request, f"Error saat membaca file Excel: {str(e)}")
            return redirect('settings')

        # Iterasi melalui data dan masukkan ke dalam model
        for index, row in df.iterrows():
            # Contoh memasukkan data ke model
            try:
                DbAllStocks.objects.create(
                    code=row['Kode'],
                    company_name=row['Nama Perusahaan'],
                    listing_board=row['Papan Pencatatan'],
                    # Tambahkan field lainnya sesuai kebutuhan
                )
            except Exception as e:
                messages.error(request, f"Error saat menyimpan data ke database: {str(e)}")
                return redirect('settings')

        messages.success(request, "Data berhasil diunggah dan disimpan ke database.")
        return redirect('settings')

    return render(request, "home/settings.html")


def hapus_data_emiten(request):
   
    if request.method == "POST":
        DbAllStocks.objects.all().delete()
        messages.success(request, f"Semua data berhasil dihapus")
        return redirect('settings')  # Ganti dengan nama view yang sesuai

    return render(request, "home/settings.html")
        