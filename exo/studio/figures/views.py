from django.views import generic

from .models import EvaluationModel3D, Model3D

# Create your views here.


class ListModel3DView(generic.ListView):
    model = Model3D

    def get_queryset(self):
        pass


class DetailModel3DView(generic.DetailView):
    pass


class ChangeModel3DView(generic.UpdateView):
    pass


class ListModel3DEvaluationView(generic.ListView):
    pass


class AddModel3DEvaluationView(generic.CreateView):
    pass


class DetailModel3DEvaluationView(generic.DetailView):
    pass
