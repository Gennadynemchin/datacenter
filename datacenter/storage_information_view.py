from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visit = {'who_entered': visit.passcard,
                            'entered_at': localtime(visit.entered_at),
                            'duration': visit.format_duration(visit.get_duration()),
                            'is_strange': visit.is_long()
                            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
