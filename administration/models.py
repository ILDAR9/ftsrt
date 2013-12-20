# -*- coding: utf-8 -*-
from django.db import models

file_content = 'administration/'


class Administration(models.Model):
    coach = models.ForeignKey('Coach', related_name="+")

    def __unicode__(self):
        return (str(self.coach)).decode('utf8')


class Document(models.Model):
    name = models.CharField(max_length=40)
    document = models.FileField(upload_to=file_content + 'files')
    info = models.CharField(blank=True, null=True, max_length=130)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Tournament(models.Model):
    name = models.CharField(max_length=30)
    organizer = models.CharField(max_length=60, blank=True, null=True)
    document = models.FileField(upload_to=file_content + 'files/calendar')
    date_start = models.DateField()
    date_end = models.DateField()
    results_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if (self.date_end < self.date_start):
            self.date_end = self.date_start
        super(Tournament, self).save()

    class Meta:
        ordering = ('name',)


class Coach(models.Model):
    fio = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, upload_to=file_content + 'avatars', null=True)
    telephone = models.CharField(blank=True, max_length=20, null=True)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(blank=True, max_length=60, null=True)

    def __unicode__(self):
        return self.fio

    # @receiver(pre_save)
    # def my_callback(instance, created, *args, **kwargs):
    #     resize(str(self.avatar))

    class Meta:
        ordering = ('fio',)


class Club(models.Model):
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    telephone2 = models.CharField(blank=True, max_length=20, null=True)
    email = models.EmailField(blank=True, null=True)
    choice_city = (
        (1, u'Казань'),
        (2, u'Набережные Челны'),
        (3, u'Нижнекамск'),
        (4, u'Альметьевск'),
        (5, u'Зеленодольск'),
        (6, u'Чистополь'),
        (7, u'Елабуга'),
        (8, u'Нурлат'),
    )
    city = models.IntegerField(blank=True, null=True, choices=choice_city)
    address = models.CharField(blank=True, max_length=40, null=True)
    url = models.URLField(blank=True, max_length=30, null=True)
    director = models.ForeignKey('Coach', blank=True, null=True)
    coaches = models.ManyToManyField(Coach, related_name='coach+')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Student(models.Model):
    stsr_id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=50)
    datebirth = models.DateField(blank=True, null=True)
    club = models.ForeignKey('Club', related_name='+')
    MALE = 'm'
    FEMALE = 'f'
    choice_gender = (
        (MALE, 'мужской'),
        (FEMALE, 'женский'))
    gender = models.CharField(max_length=1, choices=choice_gender, default=FEMALE)
    choice_class = (
        ('H', 'H'),
        ('E', 'E'),
        ('D', 'D'),
        ('C', 'C'),
        ('B', 'B'),
        ('A', 'A'),
        ('S', 'S'),
        ('M', 'M'))
    latin_level = models.CharField(max_length=1, choices=choice_class, default='H')
    standart_level = models.CharField(max_length=1, choices=choice_class, default='H')
    choice_category = (
        (0, 'нет'),
        (1, 'III юн'),
        (2, 'II юн'),
        (3, 'I юн'),
        (11, 'III'),
        (12, 'II'),
        (13, 'I'),
        (21, 'КМС'),
        (22, 'МС'),
        (23, 'МСМК'))
    category = models.SmallIntegerField(choices=choice_category, default=0)

    def __unicode__(self):
        return self.fio

    class Meta:
        ordering = ('fio',)


class Pair(models.Model):
    student_male = models.ForeignKey('Student', related_name='m+')
    student_female = models.ForeignKey('Student', related_name='f+')
    club = models.ForeignKey('Club', related_name='+')

    def __unicode__(self):
        return "%s : %s" % ((str(self.student_female)).decode('utf8'), (str(self.student_male)).decode('utf8'))

