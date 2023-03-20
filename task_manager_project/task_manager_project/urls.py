"""task_manager_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager_app.views import (
    TaskListView,
    TaskAllListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    ProjectListView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,
    SprintListView,
    SprintCreateView,
    SprintDeleteView,
    SprintUpdateView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", TaskListView.as_view(), name="task_view"),
    path("tasks_all/", TaskAllListView.as_view(), name="task_view_all"),
    path("task_create/", TaskCreateView.as_view(), name="task_crt"),
    path("task_delete/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
    path("projects/", ProjectListView.as_view(), name="projects_"),
    path("project_create/", ProjectCreateView.as_view(), name="project_crt"),
    path(
        "project_delete/<int:pk>/delete",
        ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    path("project/<int:pk>/edit", ProjectUpdateView.as_view(), name="project_edit"),
    path("sprints/", SprintListView.as_view(), name="sprints_"),
    path("sprint_create/", SprintCreateView.as_view(), name="sprint_crt"),
    path(
        "sprint_delete/<int:pk>/delete",
        SprintDeleteView.as_view(),
        name="sprint_delete",
    ),
    path("sprint/<int:pk>/edit", SprintUpdateView.as_view(), name="sprint_edit"),
    path("api/", include("task_manager_app.urls")),
    path("", include("djoser.urls.jwt")),
    # path("iommi_form/", task_form_view_iommi.as_view()),
    # path("iommi_list/", iommi_table_view),
    path("", TaskListView.as_view(), name="task_view"),
    path("accounts/", include("django.contrib.auth.urls")),
]
