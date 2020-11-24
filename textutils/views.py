# This file has created manually
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')

    # check checkbox values
    removefcn = request.POST.get('removefcn','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    #check checkbox is on
    if removefcn == "on":
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'remove punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext = analyzed



    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="/n" and char!="r":
                analyzed = analyzed + char
            else:
                print("pre",analyzed)
        params = {'purpose': 'removed Newline', 'analyzed_text': analyzed}


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if  (djtext[index]== " " and djtext[index+1]==" "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed  = len(djtext)
        params = {'purpose': 'charcount', 'analyzed_text': analyzed}
        djtext = analyzed


    if(removefcn !="on"and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("oops:please select any operation and try again")


    return render(request, 'analyze.html', params)