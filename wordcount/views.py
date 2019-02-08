from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
#    return HttpResponse('Hello')
    return render(request, 'home.html')

def aboutPage(request):
#    return HttpResponse('Hello')
    return render(request, 'about.html')

def count(request):
    wordtext = request.GET['wordtext']
    wordlist = wordtext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sortedword_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'mywordtext':wordtext, 'wordcount':len(wordlist), 'worddictionary':word_dictionary, 'word_dict_list':word_dictionary.items(), 'sortedwordlist':sortedword_list})
