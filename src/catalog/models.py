from django.db import models
from django.utils.translation import ugettext_lazy as _

class Course(models.Model):
    name = models.CharField(verbose_name=_('Назва'), max_length=200, unique=True)
    start_date = models.DateField(verbose_name=_('Дата початку'))
    end_date = models.DateField(verbose_name=_('Дата закінчення'))
    lections_quantity = models.IntegerField(verbose_name=_('Кількість лекцій'))


    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курси')


    def __str__(self):
        return self.name
    
