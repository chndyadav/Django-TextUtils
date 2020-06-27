from django.shortcuts import render
from django.http import HttpResponse
import string
import re
from django.contrib.auth import user_logged_in


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charcount = request.POST.get("charcount", "off")
    if removepunc == "on":
        puntuations = string.punctuation  # to get the punctuations
        analyzed = ""
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
        params = {"purpose": "Remove Puncs", "analyze_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {"purpose": "Convert to upper cases", "analyze_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Removed NewLines", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Remove Extra space", "analyze_text": analyzed}

        # return render(request, "analyze.html", params)

    if (
        removepunc != "on"
        and fullcaps != "on"
        and newlineremover != "on"
        and extraspaceremover != "on"
    ):
        return HttpResponse("Error")
    # elif charcount == "on":
    #     analyzed = len(djtext)
    #     params = {"purpose": "Char count", "analyze_text": analyzed}
    #     djtext = analyzed
    #     return render(request, "analyze.html", params)
    # else:
    #     return HttpResponse("Error")

    return render(request, "analyze.html", params)

