from django.db import models

class Artiles(models.Model):
    title = models.CharField('name', max_length=50)
    # , default = 'enter news name'
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('article')
    date = models.DateTimeField('publication date')

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News line'

    def get_absolute_url(self):
        return f'/news/{self.id}'
