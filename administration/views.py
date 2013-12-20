# -*- coding: utf-8 -*-
from django.contrib.redirects.models import Redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from administration.models import Administration, Document, Student, Club, Tournament, Coach, Pair
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import random

def get_administration(request):
    response = Administration.objects.select_related().all()
    return render_to_response('administration/administration.html', {'administration': response, 'text': 'asdasdasdasd'},
                              context_instance=RequestContext(request))

def get_docs(request):
    response = Document.objects.all()
    return render_to_response('administration/documents.html', {'documents': response, },
                              context_instance=RequestContext(request))

def get_clubs(request):
    response = Club.objects.select_related().all()
    return render_to_response('administration/clubs.html', {'clubs': response, },
                              context_instance=RequestContext(request))

def get_tournaments(request):
    if request.method == 'POST':
        year = request.POST.get('ShowYear')
        month = request.POST.get('ShowMonth')
        response = Tournament.objects.filter(date_start__year=year,
                                             date_start__month=month)
    else:
        response = Tournament.objects.order_by('-date_start')[:10]
    return render_to_response('administration/tournaments.html', {'tournaments': response, },
                              context_instance=RequestContext(request))

def club_detail(request, dance_club_id):
    club = get_object_or_404(Club, pk=dance_club_id)
    students = Student.objects.filter(club_id=dance_club_id)
    pairs = Pair.objects.filter(club_id=dance_club_id)
    context = {'club': club, 'students': students, 'pairs': pairs}
    return render_to_response('administration/club.html', context,
                              context_instance=RequestContext(request))

def get_coach(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    context = {'coach': coach}
    return render_to_response('administration/coach.html', context,
                              context_instance=RequestContext(request))

def any_club(request):
    id = Club.objects.order_by('?')[0].id
    return  HttpResponseRedirect(reverse('club', kwargs={'dance_club_id': id}))

def load_file(request):
    if request.method == "POST":
        file = request.FILES
        if file:
            doc = Document(name='file', document=file['document'], info='Unchecked')
            doc.save()
    return  HttpResponseRedirect(reverse('docs'))