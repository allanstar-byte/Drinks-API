from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # get all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return json
    return JsonResponse({"drinks": serializer.data}, safe=False)