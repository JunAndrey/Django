from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations_ = []
    with open("data-398-2018-08-30.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            stations_.append({})
            stations_[-1]["Name"] = row["Name"]
            stations_[-1]["Street"] = row["Street"]
            stations_[-1]["District"] = row["District"]

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations_, 10)
    page = paginator.get_page(page_number)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page}
    return render(request, 'stations/index.html', context)
