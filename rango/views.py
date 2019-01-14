from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    message = "Rango says here is the about page.<br>" + \
              "Click <a href='/'> here</a> to get back to the index page."
    return HttpResponse(message)
