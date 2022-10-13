from django.shortcuts import render


def kalenders(request):
    kalenders_list = [
        {"jaar": 2020},
        {"jaar": 2021},
        {"jaar": 2022},
    ]
    return render(
        request, "kalenders/kalenders.html", {"kalenders": kalenders_list}
    )


def kalender(request, jaar):
    return render(
        request, "kalenders/kalender.html", {"kalender": {"jaar": jaar}}
    )
