from django.db import models


class Currency(models.Model):
    name = models.CharField('Название валюты', max_length=50)
    rate = models.DecimalField('Курс к рублю', max_digits=8, decimal_places=4)
    # Я бы ещё добавил поля code and nominal для удобного поиска валюты по коду
    # и более точного отображения информации, ведь не все курсы приправниваются к 1 еденице валюты
    # code = models.CharField('Код валюты', max_length=5)
    # nominal = models.PositiveIntegerField('Номинал валюты', default=1)

    def __str__(self):
        return self.name
