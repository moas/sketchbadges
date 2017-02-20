from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views import generic

from .forms import EvaluationModel3DForm
from .models import EvaluationModel3D, Model3D

# Create your views here.


class ListModel3DView(generic.ListView):
    model = Model3D
    template_name = 'home.html'
    context_object_name = 'items'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('designer').filter(is_active=True)


class DetailModel3DView(generic.DetailView):
    template_name = 'model_detail.html'
    context_object_name = 'item'
    model = Model3D

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('designer').filter(is_active=True)


class AddModel3DEvaluationView(generic.CreateView):
    template_name = 'add_comment.html'
    model = EvaluationModel3D
    form_class = EvaluationModel3DForm

    @cached_property
    def model_3d_object(self):
        model_3d = get_object_or_404(Model3D, pk=self.kwargs['pk'])
        return model_3d

    def get_success_url(self):
        return reverse('models:detail', args=[self.model_3d_object.pk])

    def get_initial(self):
        initial = super().get_initial()
        initial['model_3d'] = self.model_3d_object
        return initial
