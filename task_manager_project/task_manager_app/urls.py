from rest_framework.routers import DefaultRouter
from task_manager_app.views import TaskViewSet, SprintViewSet, ProjectViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "task_manager_app"


router.register(
    prefix="tasks",
    viewset=TaskViewSet,
    basename="tasks",
)

router.register(
    prefix="sprints",
    viewset=SprintViewSet,
    basename="sprints",
)

router.register(
    prefix="projects",
    viewset=ProjectViewSet,
    basename="projects",
)

urlpatterns = router.urls
