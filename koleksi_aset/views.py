from django.db import connection
from django.shortcuts import redirect, render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from collections import namedtuple
from .forms import *

def list_aset(request):
    with connection.cursor() as cursor:
        cursor.execute("set search_path to public")
        role = request.session['email'][1]

        if role == "admin":
            cursor.execute("set search_path to hidayf02")
            return render(request, 'admin_list_aset.html')
        elif role == "pengguna":
            cursor.execute("set search_path to hidayf02")
            return render(request, 'pengguna_list_aset.html')

def list_dekorasi(request):
    with connection.cursor() as cursor:
        cursor.execute("set search_path to hidayf02")
        cursor.execute("SELECT * FROM ASET A INNER JOIN DEKORASI D ON A.ID = D.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil, 'nama':'Dekorasi'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)

def list_bibit_tanaman(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ASET A INNER JOIN BIBIT_TANAMAN B ON A.ID = B.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil, 'nama':'Bibit Tanaman'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)

def list_kandang(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ASET A INNER JOIN KANDANG K ON A.ID = K.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil, 'nama':'Kandang'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)

def list_hewan(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ASET A INNER JOIN HEWAN H ON A.ID = H.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil,'nama':'Hewan'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)

def list_alat_produksi(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ASET A INNER JOIN ALAT_PRODUKSI AP ON A.ID = AP.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil,'nama':'Alat Produksi'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)


def list_petak_sawah(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ASET A INNER JOIN PETAK_SAWAH P ON A.ID = P.ID_Aset")
        hasil = cursor.fetchall()
        argument = {'table':hasil,'nama':'Petak Sawah'}
        cursor.close()
        if request.session.get("role") == "admin":
            return render(request, 'admin_tabel_list_aset.html', argument)
        elif request.session.get("role") == "pengguna":
            return render(request, 'pengguna_tabel_list_aset.html', argument)
