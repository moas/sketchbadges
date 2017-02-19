import uuid

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from ..helpers.models import CommonModels

# Create your models here.


@python_2_unicode_compatible
class Model3D(CommonModels):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    designer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={
            'groups__name__in': [settings.DESIGNER_GROUP_NAME]
        }
    )
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', sep='-')
    view_counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Model 3D')
        verbose_name_plural = _('Models 3D')

    def __str__(self):
        return _("Model %(uid)s") % {'uid': self.uid.hex}

    def get_absolute_url(self):
        return reverse_lazy('figures:model-detail', self.designer.username, self.uid.hex)


@python_2_unicode_compatible
class EvaluationModel3D(CommonModels):
    model_3d = models.ForeignKey(Model3D, limit_choices_to={'is_active': True})
    commentator = models.EmailField()
    comment = models.TextField(null=True, blank=True)
    evaluation = models.IntegerField()

    class Meta:
        verbose_name = _('Evaluation')
        verbose_name_plural = _('Model evaluations')

    def __str__(self):
        return _("Comment %(pk)s") % {'pk': self.pk}
