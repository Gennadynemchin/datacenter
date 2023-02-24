from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.filter(passcode=passcode), passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        single_visit = {'entered_at': visit.entered_at,
                        'duration': visit.leaved_at - visit.entered_at,
                        'is_strange': visit.is_long()
                        }
        this_passcard_visits.append(single_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
