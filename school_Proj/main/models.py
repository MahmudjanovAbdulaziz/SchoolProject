from django.db import models, IntegrityError
from django.core.exceptions import ValidationError

# class CustomSingleError(IntegrityError):
#     def __init__(self, message='Операция запрещена: Запись уже существует.', code=4001):
#         self.message = message
#         self.code = code
#         super().__init__(self.message)

#     def __str__(self):
#         return f'[Ошибка {self.code}] {self.message}'


class Events(models.Model):
    text = models.CharField(max_length=250, verbose_name="Название события")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    img = models.ImageField(upload_to="Events", verbose_name="Изображение")

    class Meta:
        verbose_name = "События"
        verbose_name_plural = "События"


class School_cherecters_count(models.Model):
    text = models.CharField(max_length=250, verbose_name="Незначительная деталь")
    colvo_student = models.PositiveIntegerField(default=0, verbose_name="Количество студентов")
    colvo_teacher = models.PositiveIntegerField(default=0, verbose_name="Количество учителей")
    colvo_classes = models.PositiveIntegerField(default=0, verbose_name="Количество классов")
    colvo_offices = models.PositiveIntegerField(default=0, verbose_name="Количество кабинетов")

    def save(self, *args, **kwargs):
        if not self.pk and School_cherecters_count.objects.exists():
            raise ValidationError('Запись уже существует. Разрешена только одна запись для этой таблицы')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Количество учашихся"
        verbose_name_plural = "Количество учашихся"


class Teachers(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    surname = models.CharField(max_length=250, verbose_name="Фамилия")
    job_title = models.CharField(max_length=250, verbose_name="Профессия")
    img = models.ImageField(upload_to="Teachers", verbose_name="Изображение")

    class Meta:
        verbose_name = "Учителя"
        verbose_name_plural = "Учителя"


    def __str__(self):
        return self.name


class Gallery(models.Model):
    img = models.ImageField(upload_to="Gallery", verbose_name="Изображение")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class Our_graduates(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    surname = models.CharField(max_length=250, verbose_name="Фамилия")
    img = models.ImageField(upload_to="Graduates", verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наши выпускники"
        verbose_name_plural = "Наши выпускники"
