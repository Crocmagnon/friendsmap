from django.db import models


class CoordinateField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = 11
        kwargs['decimal_places'] = 8
        kwargs['help_text'] = ('Format : xxx,xxxxxxxx<br>'
                               '(max 8 decimal places, max 3 digits before comma, separator : comma)')

        super().__init__(*args, **kwargs)
