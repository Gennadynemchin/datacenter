from datacenter.models import Passcard
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def active_passcards_view(request):
    get_object_or_404(Passcard, pk=1)
    all_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_passcards,
    }
    return render(request, 'active_passcards.html', context)
