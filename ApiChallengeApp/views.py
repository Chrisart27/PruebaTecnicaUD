from django.db.transaction import atomic
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ApiChallengeApp.models import UserSelection, Candidate, Politic
import requests


def index(request):
    res = requests.get('http://www.congresovisible.org/api/apis/partidosConcejo/?format=json')
    return render(request, 'ApiChallengeApp/index.html', context={'results': res.json()['results']})


def candidates(request):
    id = request.GET.get('id', 0)
    name = request.GET.get('name', '')
    res = requests.get('http://www.congresovisible.org/api/apis/candidatos-concejo/',
                       params={'format': 'json', 'partido': id})
    return render(request, 'ApiChallengeApp/candidates.html', context={'results': res.json()['results'], 'pp_name': name})


@csrf_exempt
@atomic
def save_selection(request):
    selected_names = request.POST.getlist('selected-names', [])
    pp_name = request.POST.get('pp-name', '')
    pp_query = Politic.objects.filter(name=pp_name).first()
    if not pp_query:
        pp_query = Politic(name=pp_name)
        pp_query.save()
    candidates_queries = []
    for c in selected_names:
        c_query = Candidate.objects.filter(name=c).first()
        if not c_query:
            c_query = Candidate(name=c)
            c_query.save()
        candidates_queries.append(c_query)
    user_selection = UserSelection(fk_politic_id=pp_query.id)
    user_selection.save()
    for cq in candidates_queries:
        user_selection.candidates.add(cq)
    user_selection.save()
    res = requests.get('http://www.congresovisible.org/api/apis/partidosConcejo/?format=json')
    return render(request, 'ApiChallengeApp/index.html', context={'results': res.json()['results']})
