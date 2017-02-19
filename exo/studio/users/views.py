from django.views import generic

# Create your views here.


class UserListView(generic.ListView):
    pass


class UserRedirectView(generic.RedirectView):
    pass


class UserDetailView(generic.DetailView):
    pass


class UserUpdateView(generic.UpdateView):
    pass
