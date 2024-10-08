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
    return render(request, "home/index.html") 

def settings(request):
    return render(request, "home/settings.html")

def setting_data(request):
    
        # stocks_settings = list(DbAllStocks.objects.values('code','company_name' , 'listing_board' ))
    # page = int(request.GET.get('page', 1))  # Ambil nomor halaman dari request
    # per_page = int(request.GET.get('size', 10))  # Ambil jumlah item per halaman dari request
    # all_data_emiten = DbAllStocks.objects.all().order_by('id')

    #     # Buat pagination
    # paginator = Paginator(all_data_emiten, per_page)
    # data_page = paginator.page(page)

    # start_index = data_page.start_index() 

    # data_emiten_with_row_numbers = [
    #     {
    #         "row_number": i + start_index,  # Tambahkan nomor urut global
    #         "name": item.code,
    #         "age": item.company_name,
    #         "gender": item.listing_board,
    #         # field lainnya...
    #     }
    #     for i, item in enumerate(data_page)
    # ]

    # return JsonResponse({
    #     "data": data_emiten_with_row_numbers,
    #     "total": paginator.count,
    # })




    # return JsonResponse(all_data_emiten, safe=False) 


    # try:
    #     page = int(request.GET.get('page', 1))  # Ambil nomor halaman dari request, default 1
    # except ValueError:
    #     page = 1

    # try:
    #     per_page = int(request.GET.get('size', 10))  # Ambil jumlah item per halaman dari request, default 10
    # except ValueError:
    #     per_page = 10

    # # Tambahkan pengurutan di sini
    # all_data = DbAllStocks.objects.all().order_by('id')  # Ganti 'id' dengan field yang sesuai jika diperlukan

    # # Buat pagination
    # paginator = Paginator(all_data, per_page)

    # try:
    #     data_page = paginator.page(page)
    # except PageNotAnInteger:
    #     data_page = paginator.page(1)
    # except EmptyPage:
    #     data_page = paginator.page(paginator.num_pages)

    # # Hitung row number global
    # start_index = data_page.start_index()  # Index pertama di halaman ini (global)
    # data_with_row_numbers = [
    #     {
    #         "row_number": i + start_index,
    #         "name": item.code,
    #         "age": item.company_name,
    #         "gender": item.listing_board,
    #         # Tambahkan field lainnya sesuai kebutuhan
    #     }
    #     for i, item in enumerate(data_page)
    # ]

    # return JsonResponse({
    #     "data": data_with_row_numbers,
    #     "total": paginator.count,
    #     "total_pages": paginator.num_pages,
    # })


    page = request.GET.get('page', 1)
    size = request.GET.get('size', 15)
    
    all_data = list(DbAllStocks.objects.all().order_by('id'))  # Pastikan data diurutkan

    print(all_data)
    paginator = Paginator(all_data, size)
    
    try:
        data_page = paginator.page(page)
    except PageNotAnInteger:
        data_page = paginator.page(1)
    except EmptyPage:
        data_page = paginator.page(paginator.num_pages)
    
    # Siapkan data yang akan dikirim ke Tabulator.js
    data = [
        {
            "no": index + data_page.start_index(),  # Nomor urut global
            "code": item.code,
            "company_name": item.company_name,
            "listing_board": item.listing_board,
        }
        for index, item in enumerate(data_page)
    ]
    
    # JSON response sesuai format yang diharapkan
    return JsonResponse({
        "total_pages": paginator.num_pages,
        "data": data,
        "current_page": data_page.number
    }, safe=False)


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
        