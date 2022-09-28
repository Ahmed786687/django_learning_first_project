from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Try to get projects as a freelancer",
    "february": "Try to lose some wait",
    "march": "Don't celebrate your birth day",
    "april": "Learn Django",
    "may": "Learn Python",
    "june": "learn android development",
    "july": "Create a youtube channel on Development",
    "august": "Try to complete Google Course",
    "september": "Complete Django Course of Maxi",
    "october": "Complete Data Science course of udemy",
    "november": "complete React js course",
    "december": "Try to wind up all task of the whole year to take a new start"
}


# Create your views here.
# Http Response is used to set View for the Specific Url

def monthly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Input</h1>")
    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/"+ redirect_month) # it is not much dynamic
    # return HttpResponse(f'<h1>{months[month]}</h1>')


def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return HttpResponse(f'<h1>{challenges_text}</h1>')
    except:
        return HttpResponseNotFound("Response Not Found")

    # if month == 'january':
    #     challenges_text = "january"
    # elif month == 'february':
    #     challenges_text = 'february'
    # elif month == 'march':
    #     challenges_text = 'march'
    # elif month == 'april':
    #     challenges_text = 'april'
    # else:
    #     return HttpResponseNotFound("Not Found")

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
