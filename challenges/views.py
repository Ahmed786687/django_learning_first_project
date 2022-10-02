from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

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


def get_months_list():
    return list(monthly_challenges.keys())


# Create your views here.

def index(request):
    # list_items = []
    # items_path = []
    challenges_dict = {}
    months = get_months_list()

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        challenges_dict[month.capitalize()] = month_path
        # items_path.append(month_path)
        # # list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
        # list_items.append(month.capitalize())

    # response_data = f"<h1>All Challenges</h1><ul>{list_items}</ul>"
    # response_data = list_items
    #
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "challenges_dict": challenges_dict,
        # "month_path": month_path,
        # "month_name": month.capitalize(),
        # "items_path": items_path,
        # "list_items": list_items
        # "month": month.capitalize,
        # "text": text,
    })


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
    # months = list(monthly_challenges.keys())
    months = get_months_list()
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]

    # redirect_month has name of month so don't forget it.

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        # To load html or css content in django project, we need to include path in the setting
        # file of the main project app.
        return render(request, "challenges/challenge.html", {
            "month": month.capitalize,
            "text": text,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(f"<h1>{response_data}</h1>")
    except:
        return HttpResponseNotFound("<h1>This month is not Supported!</h1>")
