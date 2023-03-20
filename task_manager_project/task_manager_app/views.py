# from django.shortcuts import render
from task_manager_app.models import TaskModel, SprintModel, ProjectModel
from django.views.generic import (
    #DetailView,
    ListView,
    CreateView,
    UpdateView,
    #View,
    DeleteView,
)
from task_manager_app.serializers import (
    TaskSerializer,
    ProjectSerializer,
    SprintSerializer,
)
from .filters import TaskFilterSet, ProjectFilterSet, SprintFilterSet
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
# from task_manager_app.forms import TaskViewForm
# from django.views.generic.edit import FormView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# view for Task
class TaskListView(LoginRequiredMixin, ListView):
    """Представление для отображения задач."""

    context_object_name = "tasks_"
    queryset = TaskModel.objects.all()
    template_name = "task_list.html"
    # form_class = TaskViewForm
    # template_name = "bs_example.html"

    def get_queryset(self):
        # выводим только задачи, где автор - залогиненный пользователь
        queryset = (
            TaskModel.objects.all()
            .filter(task_implementer=self.request.user)
            .order_by("-id")
        )
        return queryset


class TaskAllListView(LoginRequiredMixin, ListView):
    """Представление для отображения задач."""

    context_object_name = "tasks_all_"
    queryset = TaskModel.objects.all()
    template_name = "task_list_all.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания одной задачи."""

    model = TaskModel
    fields = [
        "task",
        "task_is_Done",
        "task_plan",
        "task_author",
        "task_implementer",
        "task_attach",
        "task_project",
        "task_sprint",
    ]
    template_name = "task_create.html"
    success_url = "/tasks/"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления задачи."""

    context_object_name = "task_del"
    model = TaskModel
    fields = ["task", "task_is_Done", "task_implementer", "task_project", "task_sprint"]
    template_name = "task_delete.html"
    success_url = "/tasks/"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для изменения задачи."""

    model = TaskModel
    fields = [
        "task",
        "task_is_Done",
        "task_plan",
        "task_author",
        "task_implementer",
        "task_attach",
        "task_project",
        "task_sprint",
    ]
    template_name = "task_edit.html"
    success_url = "/tasks/"


# -------------------------------------------------------
# view for Project
class ProjectListView(LoginRequiredMixin, ListView):
    """Представление для отображения проектов."""

    context_object_name = "projects_"
    queryset = ProjectModel.objects.all()
    template_name = "project_list.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания одного проекта."""

    model = ProjectModel
    fields = ["project_name", "project_description", "project_head"]
    template_name = "project_create.html"
    success_url = "/projects/"


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления проекта."""

    context_object_name = "project_del"
    model = ProjectModel
    fields = ["project_name", "project_description", "project_head"]
    template_name = "project_delete.html"
    success_url = "/projects/"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для изменения проекта."""

    model = ProjectModel
    fields = ["project_name", "project_description", "project_head"]
    template_name = "project_edit.html"
    success_url = "/projects/"


class SprintListView(LoginRequiredMixin, ListView):
    """Представление для отображения спринтов."""

    context_object_name = "sprints_"
    queryset = SprintModel.objects.all()
    template_name = "sprint_list.html"


# -------------------------------------------------------
# view for Srint
class SprintCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания одной спринта."""

    model = SprintModel
    fields = ["sprint", "sprint_start", "sprint_end", "sprint_project"]
    template_name = "sprint_create.html"
    success_url = "/sprints/"


class SprintDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления спринта."""

    context_object_name = "sprint_del"
    model = SprintModel
    fields = ["sprint", "sprint_start", "sprint_end"]
    template_name = "sprint_delete.html"
    success_url = "/sprints/"


class SprintUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для изменения спринта."""

    model = SprintModel
    fields = ["sprint", "sprint_start", "sprint_end", "sprint_project"]
    template_name = "sprint_edit.html"
    success_url = "/sprints/"


# -------------------------------------------------------
# viewset DRF - task
class TaskViewSet(
    mixins.ListModelMixin,  # GET /tasks
    mixins.CreateModelMixin,  # POST /tasks
    mixins.RetrieveModelMixin,  # GET /tasks/1
    mixins.DestroyModelMixin,  # DELETE /tasks/1
    mixins.UpdateModelMixin,  # PUT /tasks/1
    viewsets.GenericViewSet,
):
    queryset = TaskModel.objects.all().order_by("-id")
    serializer_class = TaskSerializer

    filterset_class = TaskFilterSet
    # pagination_class = None
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# -------------------------------------------------------
# viewset DRF - project
class ProjectViewSet(
    mixins.ListModelMixin,  # GET /projects
    mixins.CreateModelMixin,  # POST /projects
    mixins.RetrieveModelMixin,  # GET /projects/1
    mixins.DestroyModelMixin,  # DELETE /projects/1
    mixins.UpdateModelMixin,  # PUT /projects/1
    viewsets.GenericViewSet,
):
    queryset = ProjectModel.objects.all().order_by("-id")
    serializer_class = ProjectSerializer

    filterset_class = ProjectFilterSet
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# -------------------------------------------------------
# viewset DRF - sprint
class SprintViewSet(
    mixins.ListModelMixin,  # GET /sprints
    mixins.CreateModelMixin,  # POST /sprints
    mixins.RetrieveModelMixin,  # GET /sprints/1
    mixins.DestroyModelMixin,  # DELETE /sprints/1
    mixins.UpdateModelMixin,  # PUT /sprints/1
    viewsets.GenericViewSet,
):
    queryset = SprintModel.objects.all().order_by("-id")
    serializer_class = SprintSerializer

    filterset_class = SprintFilterSet
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
