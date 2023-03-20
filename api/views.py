from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def drink_list(request):
    # get all the drinks
    # serialize them
    # return json
