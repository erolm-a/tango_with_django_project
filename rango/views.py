from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'footerSection': "This tutorial has been put together by erolm_a"}

    return render(request, 'rango/about.html', context=context_dict)
