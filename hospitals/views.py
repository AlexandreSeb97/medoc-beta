from django.shortcuts import render
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from .models import Hospital
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, redirect

# Hospitals view
def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home',
            'year':datetime.now().year,
            'date':datetime.now().date,
        })
    )

def hospital(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital = Hospital.objects.all()
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'hospitals.html',
        {'hospitals': hospital},
        context_instance = RequestContext(request,
        {
            'title': 'Hospitals',
            'message': 'List of all Hospitals in MeDOC',
            'year': datetime.now().year,
        })
    )

def hospital_fr(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital = Hospital.objects.all()
    return render(request, 'hospitals/hospitals_fr.html', {'hospitals': hospital})
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'hospitals_fr.html',
        context_instance = RequestContext(request,
        {
            'title': 'Hopitaux',
            'message': 'List of all Hospitals in MeDOC',
            'year': datetime.now().year,
        })
    )

def hospital_kr(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital_list = Hospital.objects.all()
    return render(request, 'hospitals/hospitals_kr.html', {'hospitals': hospital})
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'hospitals_kr.html',
        context_instance = RequestContext(request,
        {
            'title': 'Lopital',
            'message': 'List of all Hospitals in MeDOC',
            'year': datetime.now().year,
        })
    )
