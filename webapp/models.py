from django.db import models


# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Sketchpad(models.Model):
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")
    created_note = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    date_of_completion = models.DateField(auto_now=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status} {self.date_of_completion}"

    class Meta:
        db_table = "sketchpad"
        verbose_name = "задача"
        verbose_name_plural = "Список задач"