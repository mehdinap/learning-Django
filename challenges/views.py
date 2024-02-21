from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


mothlly_challenges = {
    "january": "This is january!",
    "february": "This is february!",
    "murch": "This is murch!",
    "april": "This is april!",
    "may": "This is may!",
}


def index(request):
    list_item = ""
    months = list(mothlly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_item += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_numbers(request, month):
    months = list(mothlly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This is not supported!")
    redirect_month = months[month - 1]
    # by HttpResponseRedirect func we redirect url to month and do by
    # monthly_challenges function with str:month url
    # when it works, redirect and execute with code's 302

    redirect_path = reverse(
        "month_challenge", args=[redirect_month]
    )  # /challenge/MONTH'S_NAME
    # alternative of following line code, we use refirect_path
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challeng_data = mothlly_challenges[month]
        return render( request,"challenges/challenges.html",{
            "text":challeng_data
        })
        # response_data = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not supported!</h1>")
