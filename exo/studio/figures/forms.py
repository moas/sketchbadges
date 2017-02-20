from django import forms

from .models import Model3D, EvaluationModel3D


class AddModel3DForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self._request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Model3D
        fields = ('name', )

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.designer = self._request.user
        if commit:
            obj.save()
        return obj


class ChangeModel3DForm(AddModel3DForm):

    class Meta(AddModel3DForm.Meta):
        fields = ('name', 'is_active')


class EvaluationModel3DForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_3d'].widget = forms.HiddenInput()

    class Meta:
        model = EvaluationModel3D
        exclude = ('is_active', )
