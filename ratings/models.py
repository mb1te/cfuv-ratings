from django.db import models


class Abiturient(models.Model):

    fio = models.CharField(max_length=255, default='')
    field = models.CharField(max_length=255, default='')
    is_accepted = models.BooleanField(default=False)
    type = models.CharField(max_length=255, default='')
    form = models.CharField(max_length=255, default='')
    res_sum = models.IntegerField(default=0)
    min_ball = models.IntegerField(default=0)
    cnt_of_places = models.IntegerField(default=0)
    cur_place = models.IntegerField(default=0)

    def __str__(self):
        return self.fio


class FieldOfStudy(models.Model):

    type = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name + " " + self.type
