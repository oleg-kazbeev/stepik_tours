from django.views.generic import View
from django.http import HttpResponseNotFound
from django.shortcuts import render
from data import tours, departures


class MainView(View):

    def get(self, request, *args, **kwargs):
        tour_id = (1, 3, 5, 7, 10, 12)
        six_random_tours = {k: tours[k] for k in tour_id}
        return render(request, "index.html", {"tours": six_random_tours})


class DepartureView(View):
    def get(self, request, departure):
        sorted_tours_by_departure = {k: v for k, v in tours.items() if v["departure"] == departure}
        data = {"tours": sorted_tours_by_departure, "departure": departures[departure]}
        return render(request, "departure.html", context=data)


class TourView(View):
    def get(self, request, id):
        return render(request, "tour.html", tours[id])


def custom_handler404(request, exception):
    return HttpResponseNotFound('Что-то пошло не так...')


def custom_handler500(request, exception):
    return HttpResponseNotFound('К сожалению, данный ресурс временно не доступен :(')
