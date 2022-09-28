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

# -----------Manual method - Method 1
# def index(request):
#     return HttpResponse("<h1>This works</h1>")


# # ------------Normal-Dynamic Method for generating view - Method 2
# def monthly_challenge_by_number(request, month):
#     return HttpResponse(month)
#
#
# def monthly_challenge(request, month):
#     text = "Not Found"
#     if month == 'january':
#         text = "I am Jan"
#     elif month == "february":
#         text = "I'm February"
#     return HttpResponse(text)

# # # ------------Standard-Dynamic Method for generating view - Method 2
# def monthly_challenge(request, month):
#     try:
#         text = monthly_challenges[month]
#         return HttpResponse(text)
#     except:
#         return HttpResponseNotFound("Month Not Found")


# # # ------------Simple Method Redirecting Urls - Method 1
# def monthly_challenge_by_number(request, month):
#     months = list(monthly_challenges.keys())
#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")
#     redirect_month = months[month - 1]
#     return HttpResponseRedirect("/challenges/" + redirect_month) #this is not dynamic yet
#
#
# def monthly_challenge(request, month):
#     try:
#         text = monthly_challenges[month]
#         return HttpResponse(text)
#     except:
#         return HttpResponseNotFound("Month Not Found")
#


# # ------------Dynamic Method of Redirecting Urls - Advance Method
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]

    # redirect_month has name of month so don't forget it.

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Month Not Found")
