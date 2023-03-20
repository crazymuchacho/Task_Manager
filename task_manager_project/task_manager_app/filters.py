from django_filters import rest_framework as dj_filters
from .models import TaskModel, SprintModel, ProjectModel


class TaskFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    task = dj_filters.CharFilter(field_name="task", lookup_expr="icontains")
    is_active = dj_filters.BooleanFilter(field_name="task_is_Done")
    task_author = dj_filters.CharFilter(field_name="task_author")
    task_implementer = dj_filters.CharFilter(field_name="task_implementer")
    task_project = dj_filters.CharFilter(field_name="task_project")
    task_sprint = dj_filters.CharFilter(field_name="task_sprint")

    order_by_field = "ordering"

    class Meta:
        model = TaskModel
        fields = [
            "task",
        ]


class ProjectFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    project_name = dj_filters.CharFilter(
        field_name="project_name", lookup_expr="icontains"
    )
    project_head = dj_filters.CharFilter(field_name="project_head")

    order_by_field = "ordering"

    class Meta:
        model = ProjectModel
        fields = [
            "project_name",
        ]


class SprintFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    sprint = dj_filters.CharFilter(field_name="sprint", lookup_expr="icontains")
    sprint_start = dj_filters.DateTimeFilter(
        field_name="sprint_start", lookup_expr="icontains"
    )
    sprint_end = dj_filters.DateTimeFilter(
        field_name="sprint_end", lookup_expr="icontains"
    )
    sprint_project = dj_filters.CharFilter(field_name="sprint_project")

    order_by_field = "ordering"

    class Meta:
        model = SprintModel
        fields = [
            "sprint",
        ]
