from django.shortcuts import render

# Create your views here.
from webapp.models import Sketchpad


def index_view(request):
    sketchpads = Sketchpad.objects.order_by("date_of_completion")
    context = {"sketchpads": sketchpads}
    return render(request, "index.html", context)

def sketchpad_view(request):
    pk = request.GET.get("pk")
    sketchpad = Sketchpad.objects.get(pk=pk)
    return render(request, "sketchpad_view.html", {"sketchpad": sketchpad})


def create_sketchpad(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        date_of_completion = request.POST.get("date_of_completion")
        new_sketchpad = Sketchpad.objects.create(description=description, status=status, date_of_completion=date_of_completion)
        context = {"sketchpad": new_sketchpad}
        return render(request, "sketchpad_view.html", context)