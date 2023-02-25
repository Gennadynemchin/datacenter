from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    return f'{hours}h {minutes}min'


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visit = {'who_entered': visit.passcard,
                            'entered_at': localtime(visit.entered_at),
                            'duration': format_duration(visit.get_duration()),
                            'is_strange': visit.is_long()
                            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
