from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, redirect

# Create your views here.


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Who are we?',
            'message':'Learn about the men behind MeDOC and SHARPRISE',
            'year':datetime.now().year,
        })
    )


def about(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Who are we?',
            'message':'Learn about the men behind MeDOC and SHARPRISE',
            'year':datetime.now().year,
        })
    )