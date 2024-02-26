from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.indexone)
    
    # use this way to avoid more increment urls and views.
    # <month> like parameter which decalaration in monthly_challenges function.
    path("",views.index,name="index"),
    path("<int:month>", views.monthly_challenges_by_numbers),
    path("<str:month>", views.monthly_challenges, name = "month_challenge"),
    
    
    
    
]