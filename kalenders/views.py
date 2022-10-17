from django.shortcuts import render

from .models import Kalender


def kalenders(request):
    kalenders_list = Kalender.objects.all().order_by("-jaar")
    return render(
        request, "kalenders/kalenders.html", {"kalenders": kalenders_list}
    )


def kalender(request, jaar):
    current_kalender = Kalender.objects.get(jaar=f"{jaar}")
    return render(
        request, "kalenders/kalender.html", {"kalender": current_kalender}
    )
