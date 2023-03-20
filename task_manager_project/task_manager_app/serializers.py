from rest_framework import serializers
from task_manager_app.models import TaskModel, SprintModel, ProjectModel
# from django.contrib.auth import get_user_model


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор по модели task."""

    class Meta:
        model = TaskModel
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "task",
            "task_is_Done",
            "task_create",
            "task_completed",
            "task_plan",
            "task_author",
            "task_implementer",
            "task_attach",
            "task_project",
            "task_sprint",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор по модели project."""

    class Meta:
        model = ProjectModel
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "project_name",
            "project_description",
            "project_head",
        ]


class SprintSerializer(serializers.ModelSerializer):
    """Сериализатор по модели sprint."""

    class Meta:
        model = SprintModel
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "sprint",
            "sprint_start",
            "sprint_end",
            "sprint_project",
        ]

        # fields = "__all__"
        # exclude = []
