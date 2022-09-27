from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
# Http Response is used to set View for the Specific Url

def monthly_challenge(request, month):
    challenges_text = 'None'
    if month == 'january':
        challenges_text = "january"
    elif month == 'february':
        challenges_text = 'february'
    elif month == 'march':
        challenges_text = 'march'
    elif month == 'april':
        challenges_text = 'april'
    else:
        return HttpResponseNotFound("Not Found")
    return HttpResponse(challenges_text)

# def january(request):
#     return HttpResponse("<h1>This works!</h1>")
#
#
# def february(request):
#     return HttpResponse("I am Fabulus")
#
#
# def march(request):
#     return HttpResponse("I am Master AIB")
#
#
# def april(request):
#     return HttpResponse("I am Ahmad Iqbal Bhatti")
#
#
# def may(request):
#     return HttpResponse("I am the Master piece")
#
#
# def june(request):
#     return HttpResponse("I am not Jealous")
#
#
# def july(request):
#     return HttpResponse("I love jalabies")
#
#
# def august(request):
#     return HttpResponse("Its independent day")
#
#
# def september(request):
#     return HttpResponse("I am Very serious about her")
#
#
# def october(request):
#     return HttpResponse("I don't like Octopus")
#
#
# def november(request):
#     return HttpResponse("There is no way to home")
#
#
# def december(request):
#     return HttpResponse("Haha deliberate")
#
#
#
#
#



