from datacenter.models import Passcard, Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        one_visit = {'entered_at': visit.entered_at,
                     'duration': visit.leaved_at - visit.entered_at,
                     'is_strange': visit.is_long()
                     }
        this_passcard_visits.append(one_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }


    return render(request, 'passcard_info.html', context)
