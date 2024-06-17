from django.http import HttpResponse
from django.shortcuts import render
from visits.models import pageVisit


def home_page_view(request,*args, **kwargs):
    my_title = "My Page"
    my_context ={
        "page_title":my_title
    }
    html_template = "home.html"
    pageVisit.objects.create()
    return render(request,"home.html")