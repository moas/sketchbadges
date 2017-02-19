from django.contrib import admin

from .models import EvaluationModel3D, Model3D

# Register your models here.


class AdminMixin:

    def get_fields(self, request, obj=None):
        """
        Use to move 'is_active' field to last position
        :param request:
        :param obj:
        :return:
        """
        fields = super().get_fields(request, obj)
        fields = [field for field in fields if field != 'is_active']
        fields.append('is_active')
        return fields


class EvaluationModel3DInline(AdminMixin, admin.StackedInline):
    model = EvaluationModel3D
    extra = 1


@admin.register(Model3D)
class Model3DAdmin(AdminMixin, admin.ModelAdmin):
    list_display = ('name', 'view_counter', 'created', 'updated')
    list_filter = ('created', 'updated')
    inlines = [EvaluationModel3DInline]
    readonly_fields = ('view_counter', )
