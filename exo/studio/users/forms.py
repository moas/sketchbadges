from django import forms
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class DesignerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('gender', 'username', 'name')

    def save(self, commit=True):
        obj = super().save(commit)
        group, _ = Group.objects.get_or_create(name=settings.DESIGNER_GROUP_NAME)
        obj.groups.add(group)
        return obj


class DesignerChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('gender', 'name', 'password', )
