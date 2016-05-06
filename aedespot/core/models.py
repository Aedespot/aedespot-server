from django.db import models


class Report(models.Model):
    '''
    Model that represents a given report by an user.
    It contains information about the location of
    the report as well as the type and timestamp.
    '''

    REPORT_CATEGORIES = (
        ('F', 'Foco'),  # Represents a potential place where aedes can appear
        ('C', 'Criadouro'),  # Represents aedes' larva on a spot
        ('S', 'Suspeita de doença'),  # Someone near having symptoms
    )

    type = models.CharField('tipo', max_length=2, choices=REPORT_CATEGORIES)
    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    reported_at = models.DateTimeField('reportado em', auto_now_add=True)

    class Meta:
        ordering = '-reported_at',
        verbose_name = 'ocorrência'
        verbose_name_plural = 'ocorrências'

    def __str__(self):
        return '({}, {}) - {}'.format(self.latitude, self.longitude, self.type)
