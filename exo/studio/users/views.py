from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth import get_user_model

from studio.helpers.mixins import DesignerGroupMixin
from studio.figures.models import Model3D
from studio.figures.forms import AddModel3DForm, ChangeModel3DForm
from .forms import DesignerChangeForm, DesignerCreationForm

# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserRedirectView(DesignerGroupMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('user:detail', args=[self.request.user.pk])


class UserDesignerCreateAccount(generic.CreateView):
    model = get_user_model()
    form_class = DesignerCreationForm
    template_name = 'add_designer.html'

    def get_success_url(self):
        return reverse('user:login')


@method_decorator(login_required, name='dispatch')
class UserDetailView(DesignerGroupMixin, generic.DetailView):
    model = get_user_model()
    template_name = 'designer_details.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(pk=self.request.user.pk)
        return qs


@method_decorator(login_required, name='dispatch')
class UserUpdateView(DesignerGroupMixin, generic.UpdateView):
    model = get_user_model()
    form_class = DesignerChangeForm
    template_name = 'change_designer.html'

    def get_success_url(self):
        return reverse('user:detail', args=[self.request.user.pk])

    def get_initial(self):
        initial = super().get_initial()
        initial.update({'request': self.request})
        return initial

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(pk=self.request.user.pk)
        return qs


@method_decorator(login_required, name='dispatch')
class DesignerListModelView(DesignerGroupMixin, generic.ListView):
    model = Model3D
    template_name = 'designer_model_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(designer=self.request.user)


@method_decorator(login_required, name='dispatch')
class DesignerAddModelView(DesignerGroupMixin, generic.CreateView):
    model = Model3D
    template_name = 'designer_add_model.html'
    form_class = AddModel3DForm

    def get_success_url(self):
        return reverse('user:model-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


@method_decorator(login_required, name='dispatch')
class DesignerChangeModelView(DesignerGroupMixin, generic.UpdateView):
    model = Model3D
    template_name = 'designer_change_model.html'
    slug_url_kwarg = 'uid'
    slug_field = 'uid'
    form_class = ChangeModel3DForm

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(designer=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('user:model-list')


@method_decorator(login_required, name='dispatch')
class DesignerModelDetailView(DesignerGroupMixin, generic.DetailView):
    model = Model3D
    template_name = 'designer_model_details.html'
    slug_url_kwarg = 'uid'
    slug_field = 'uid'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(designer=self.request.user)
        return qs
