from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def storage_information_view(request):
    get_object_or_404(Passcard, pk=1)
    get_object_or_404(Visit, pk=1)
    non_closed_visits = []
    for user in Visit.objects.filter(leaved_at=None):
        non_closed_visit = {'who_entered': user.passcard,
                            'entered_at': localtime(user.entered_at),
                            'duration': localtime() - localtime(user.entered_at),
                            'is_strange': user.is_long()
                            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
