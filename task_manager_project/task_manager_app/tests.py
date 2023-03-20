from django.test import TestCase
from task_manager_app.models import TaskModel #, SprintModel, ProjectModel
from requests import head

# Create your tests here.


class TaskTests(TestCase):
    """Тесты для модели task"""

    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.task_tests = TaskModel.objects.create(
            task="Описание задачи = 1024 символов. Тестирование.",
            task_plan="2023-03-22 09:57:48",
        )
        cls.task = cls.task_tests._meta.get_field("task")

    def test_help_text(self):
        """Тест параметра help_text"""

        real_help_text = getattr(self.task, "help_text")
        expected_help_text = "Описание задачи"
        self.assertEqual(real_help_text, expected_help_text)

    def test_max_length(self):
        """Тест параметра max_length"""

        real_max_length = getattr(self.task, "max_length")
        self.assertEqual(real_max_length, 1024)

    # def test_string_representation(self):
    #     """Тест строкового отображения"""

    #     self.assertEqual(str(self.task_tests), str(self.task_tests.task))


# response = head('http://127.0.0.1:8000/')
# print(response.status_code)

# DOMAIN = 'http://127.0.0.1:8000/'

# PAGES = (
#     '',
#     'tasks_all/',
#     'projects/',
#     'sprints/',
#     'tasks/',
#     # ...
# )
# PAGES_acc = ('accounts/login/')
# PAGES_to_account = (DOMAIN + page for page in PAGES)
# PAGES_acc = (DOMAIN + page for page in PAGES_acc)

# class PagesTests(TestCase):
#     """Класс с тестами страниц"""

#     def test_status_code(self):
#         """Тест статус-кода"""

#         for page in PAGES_to_account:
#             with self.subTest(f'{page=}'):
#                 response = head(page) # (1)

#                 self.assertEqual(response.status_code, 302) # (2) и (3)

#     def test_status_code_200(self):
#         """Тест статус-кода"""

#         for page in PAGES_acc:
#             with self.subTest(f'{page=}'):
#                 response = head(page) # (1)

#                 self.assertEqual(response.status_code, 200) # (2) и (3)
