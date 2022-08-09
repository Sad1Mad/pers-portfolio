from django.shortcuts import render
from .models import Learn


def all_learns(request):
    learns = Learn.objects.order_by("-dataLearn")
    strCount = (request.GET.get("c"))
    view_learns = learns[(5*int(strCount)):(5+5*int(strCount))]
    displayBack = "none"
    displayNext = "none"
    if int(strCount) > 0:
        displayBack = "inline-block"
    if int(strCount)+1 < len(learns)/5:
        displayNext = "inline-block"
    return render(request, "learns/learns.html", {"learns": view_learns, "disback": displayBack, "disnext": displayNext, "strcount": strCount, "back": str(int(strCount) - 1), "next": str(int(strCount) + 1)})

def open_learn(request):
    idLearn = (request.GET.get("id"))
    post_learn = Learn.objects.get(id=idLearn)
    return render(request, "learns/postlearn.html", {"post": post_learn, "id": idLearn})
