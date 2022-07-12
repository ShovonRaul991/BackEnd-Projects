from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User, ToDo

'''
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def extract_keywords(request):
    text = request.POST.get('text')
    return JsonResponse(text)
'''


# Create your views here.

def Hello_world(request):
    return HttpResponse("Hello world, you built an api")

def add(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    c = a+b
    response_of_json = {
        "message":"Success",
        "sum" : c
    }
    #return HttpResponse("The sum is: "+ str(c))
    return HttpResponse(json.dumps(response_of_json))
    #return JsonResponse(response_of_json, status = 200)


def create_user(request):
    data = json.loads(request.body)
    #print(data)  # in postman if we send a json file in row of the body we will get return here in the terminal
    fields = ["name", "date_of_birth"]

    """
    #define failed response json
    Failed_response = {
        "message": "The field should be properly given!!"
    }
    """

    for field in fields:
        if field not in data.keys():
            return JsonResponse({
                "message": field+ " is mandetory",
            },status =400)

    #user object creation
    User.objects.create(name = data["name"], date_of_birth = data["date_of_birth"])
    user_o = User.objects.get(name=data["name"])
    """
    response_of_json1 = {
        "name": user_o.name,
        "ID": user_o.id,
        "date_of_birth": user_o.date_of_birth
    }
    """
    #return HttpResponse(json.dumps(response_of_json1))
    return JsonResponse({
        "name": user_o.name,
        "ID": user_o.id,
        "date_of_birth": user_o.date_of_birth
    },status = 201)


def get_user(request):
    try:
        id = int(request.GET.get("id"))
        user = User.objects.get(pk=id)
        return JsonResponse({
            "name": user.name,
            "ID": user.id,
            "date_of_birth": user.date_of_birth
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "message": e.__str__()
        },status=404)
