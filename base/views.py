from django.shortcuts import render
from base.forms import ReservaForm


# Create your views here.
from django.shortcuts import render, redirect
from base.forms import ReservaForm


def reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            return redirect("sucesso")
    else:
        form = ReservaForm()
    return render(request, "reserva.html", {"form": form})


def sucesso(request):
    return render(
        request,
        "sucesso.html",
    )
