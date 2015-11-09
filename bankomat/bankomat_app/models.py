# _*_ coding: utf-8 _*_ #

from django.db import models
 
# Create your models here.
class Cardowner(models.Model):
    """Cardowner"""

    class Meta(object):
        verbose_name = u'Владелец карты'
        verbose_name_plural = u"Владельцы карты"
        ordering = ('last_name',) # sorted by lats_name (default)

	# Добавляем метод для удобного представления в shell и Django админке
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
			

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Имя")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Фамилия")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Отчество",
        default='')

    cardnumber = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Номер карты")

    pin_code = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Пин-код")

    balance = models.FloatField(
        blank=False,
        verbose_name=u"Баланс",
        default=0)

    card_block = models.BooleanField(
        max_length=256,
        default=False)


class Operations(models.Model):
    """Operations"""

    class Meta(object):
        verbose_name = u'Операции карты'
        verbose_name_plural = u"Операции карт"

	# Добавляем метод для удобного представления в shell и Django админке
    def __unicode__(self):
        return u"%s %s" % (self.oper_code, self.oper_table)

    oper_code = models.IntegerField(
        blank=False,
        verbose_name=u"номер операции",
        default=0)

    description = models.TextField(
		blank=True,
		verbose_name=u"Описание")

    oper_table = models.ForeignKey('Cardowner',
        verbose_name=u"Владелец карты")

    data = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Дата операции")
