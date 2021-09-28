import operator

from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    context = {"name": "John Doe"}
    return render(request, 'home.html', context)


def count(request):
    fulltext = request.GET["fulltext"]
    wordcount = fulltext.split()
    worddictionary = {}
    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_dictionary = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    context = {'fulltext': fulltext, "wordcount": len(wordcount), 'worddictionary': sorted_dictionary}
    return render(request, 'count.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
