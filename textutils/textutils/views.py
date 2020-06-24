from django.shortcuts import render
from django.http import HttpResponse
import string
from django.contrib.auth import user_logged_in


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.GET.get("text", "default")
    removepunc = request.GET.get("removepunc", "off")
    if removepunc == "on":
        puntuations = string.punctuation  # to get the punctuations
        print(puntuations)
        analyzed = ""
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove Puncs", "analyze_text": analyzed}
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")

