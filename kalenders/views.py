from django.shortcuts import render


def kalenders(request):
    return render(request, "kalenders/kalenders.html")
