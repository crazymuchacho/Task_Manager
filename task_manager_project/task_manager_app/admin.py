from django.contrib import admin
from .models import TaskModel, SprintModel, ProjectModel

# Register your models here.
# admin.site.register(TaskModel)
# admin.site.register(SprintModel)
# admin.site.register(ProjectModel)


@admin.register(SprintModel)
class SprintAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sprint",
        "sprint_start",
        "sprint_end",
        "sprint_project",
    )

    search_fields = ["sprint"]  # по каким полям будет производиться поиск


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "task_is_Done",
        "task_plan",
        "task_completed",
        "task_author",
        "task_implementer",
        "task_attach",
        "task_project",
        "task_sprint",
    )

    search_fields = ["task"]  # по каким полям будет производиться поиск


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project_name",
        "project_description",
        "project_head",
    )

    search_fields = [
        "project_name",
        "project_description",
    ]  # по каким полям будет производиться поиск
