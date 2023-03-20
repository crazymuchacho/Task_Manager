from django.db import models
from django.conf import settings
# from django_extensions.db.models import TimeStampedModel
import datetime
import requests

# Create your models here.

class ProjectModel(models.Model):
    """Модель проектов"""

    project_name = models.CharField(max_length=256, help_text="Название проекта")
    project_description = models.CharField(
        max_length=1024, help_text="Описание проекта"
    )
    project_head = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_project_head",
        null=True,
        blank=True,
        help_text="Руководитель проекта",
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Project {self.id}| {self.project_name}| {self.project_head}"


class TaskModel(models.Model):
    """Задачи"""

    task = models.CharField(max_length=1024, help_text="Описание задачи")
    task_is_Done = models.BooleanField(
        default=False, help_text="Статус выполнения задачи"
    )
    task_create = models.DateTimeField(
        auto_now_add=True, help_text="Дата/время создания задачи"
    )
    task_completed = models.DateTimeField(
        blank=True, null=True, help_text="Дата/время завершения задачи"
    )
    task_plan = models.DateTimeField(
        blank=True, null=True, help_text="Плановая дата исполнения"
    )
    task_author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_task_author",
        null=True,
        blank=True,
        help_text="Автор задачи",
    )
    task_implementer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_task_implementer",
        null=True,
        blank=True,
        help_text="Исполнитель задачи",
    )
    task_attach = models.FileField(blank=True, null=True, help_text="Вложение")
    task_project = models.ForeignKey(
        to="task_manager_app.ProjectModel",
        on_delete=models.SET_NULL,
        related_name="project_task",
        null=True,
        blank=True,
        help_text="Проект",
    )
    task_sprint = models.ForeignKey(
        to="task_manager_app.SprintModel",
        on_delete=models.SET_NULL,
        related_name="sprint_task",
        null=True,
        blank=True,
        help_text="Спринт",
    )

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.
        время завершения пустое, если не стоит Done, иначе время завершения равно времени установки статуса завершения.
        + Оповещение в группу телеграмм
        """
        if self.task_is_Done is False:
            self.task_completed = None
            message = f" Внесены изменения в {self.__str__()}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

        else:
            time_now = datetime.datetime.utcnow()
            self.task_completed = time_now
            message = f"Задача выполнена {self.__str__()}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

        return super().save(*args, **kwargs)

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Task {self.id}/{self.task}/{self.task_is_Done}/{self.task_implementer}"


class SprintModel(models.Model):
    """модель спринтов"""

    sprint = models.CharField(max_length=1024, help_text="Описание спринта")
    sprint_create = models.DateTimeField(
        auto_now_add=True, help_text="Дата/время создания спринта"
    )
    sprint_start = models.DateTimeField(help_text="Дата/время начала спринта")
    sprint_end = models.DateTimeField(help_text="Дата/время завершения спринта")
    sprint_project = models.ForeignKey(
        to=ProjectModel,
        on_delete=models.SET_NULL,
        related_name="project_sprint",
        null=True,
        blank=True,
        help_text="Проект",
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return (
            f"Спринт {self.id}/ {self.sprint}/ {self.sprint_start}/ {self.sprint_end}"
        )


TOKEN = "6153782950:AAE05hNPAzLjxfiLgKAgBShOAzQ-8N0RkTI"
chat_id = "280818126"
