from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import SketchpadForm
from webapp.models import Sketchpad, STATUS_CHOICES


def index_view(request):
    sketchpads = Sketchpad.objects.order_by("date_of_completion")
    context = {"sketchpads": sketchpads}
    return render(request, "index.html", context)


def sketchpad_view(request, **kwargs):
    pk = kwargs.get("pk")
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    return render(request, "sketchpad_view.html", {"sketchpad": sketchpad})


def create_sketchpad(request):
    if request.method == "GET":
        form = SketchpadForm()
        # return render(request, "create.html", {"statuses": STATUS_CHOICES}, {"form": form})
        return render(request, "create.html", {"form": form})
    else:
        form = SketchpadForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            date_of_completion = form.cleaned_data.get("date_of_completion")
            new_sketchpad = Sketchpad.objects.create(title=title, description=description, status=status,
                                                     date_of_completion=date_of_completion)
            return redirect("sketchpad_view", pk=new_sketchpad.pk)
        return render(request, "create.html", {"form": form})


def update_sketchpad(request, pk):
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    if request.method == "GET":
        form = SketchpadForm(initial={
            "title": sketchpad.title,
            "description": sketchpad.description,
            "status": sketchpad.status,
            "date_of_completion": sketchpad.date_of_completion
        })
        return render(request, "update.html", {"form": form})
    else:
        form = SketchpadForm(data=request.POST)
        if form.is_valid():
            sketchpad.title = form.cleaned_data.get("title")
            sketchpad.description = form.cleaned_data.get("description")
            sketchpad.status = form.cleaned_data.get("status")
            sketchpad.date_of_completion = form.cleaned_data.get("date_of_completion")
            sketchpad.save()
            return redirect("sketchpad_view", pk=sketchpad.pk)
        return render(request, "update.html", {"form": form})


def delete_sketchpad(request, pk):
    sketchpad = get_object_or_404(Sketchpad, pk=pk)
    if request.method == "GET":
        pass
    #     return render(request, "delete.html", {"article": article})
    else:
        sketchpad.delete()
        return redirect("index")
