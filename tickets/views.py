from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Guest, Movie, Reservation 
from .serializers import MovieSerializer,ReservationSerializer,GuestSerializer


# Create your views here.


#1 without REST and no model query FBV
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            "Name": "Omar",
            "mobile": 789456,
        },
        {
            'id': 2,
            'name': "yassin",
            'mobile': 74123,
        }
    ]
    return JsonResponse (guests, safe=False)

#2 model data default djanog without rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name','mobile'))
    }
    return JsonResponse(response)