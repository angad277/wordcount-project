from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'About.html')

def count(request):
    fulltext = request.GET['fulltext']

    worddictionary= {}
    wordlist = fulltext.split()
    for word in wordlist:
        if word in worddictionary:
            #increment
            worddictionary[word] += 1
        else:
            #Add to dictionary
            worddictionary[word] = 1
    return render(request, 'Count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary' : worddictionary.items()})

