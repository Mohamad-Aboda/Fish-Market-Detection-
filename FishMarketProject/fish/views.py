from django.shortcuts import render
from django.http import request
import joblib
# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    LR = joblib.load('finalmodel.sav')
    lst = []

    lst.append(request.GET['Length1'])
    lst.append(request.GET['Length2'])
    lst.append(request.GET['Length3'])
    lst.append(request.GET['Height'])
    lst.append(request.GET['Width'])
    lst.append(request.GET['Species_Bream'])
    lst.append(request.GET['Species_Parkki'])
    lst.append(request.GET['Species_Perch'])
    lst.append(request.GET['Species_Pike'])
    lst.append(request.GET['Species_Roach'])
    lst.append(request.GET['Species_Smelt'])
    lst.append(request.GET['Species_Whitefish'])

    # # lst.reshape(1, -1)
    # lst.reshape(-1, 1)
    ans = LR.predict([lst])
    return render(request, 'result.html', {'ans':ans, 'lst':lst})


def plots(request):
    return render(request, 'plots.html')


def histo(request):
    return render(request, 'histo.html')


def info(request):
    return render(request, 'info.html')

