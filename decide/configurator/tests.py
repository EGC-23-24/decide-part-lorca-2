from django.urls import reverse
from django.contrib.messages import get_messages
from django.template import TemplateDoesNotExist
from base.tests import BaseTestCase
from .forms import ClassicForm, MultipleChoiceForm, OpenQuestionForm


class ConfiguratorViewTest(BaseTestCase):
    def test_configurator_view(self):
        response = self.client.get(reverse("configurator"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/configurator.html")


class CreateClassicViewTest(BaseTestCase):
    def test_get_request(self):
        response = self.client.get(reverse("create_classic"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_classic.html")
        self.assertIsInstance(response.context["form"], ClassicForm)

    def test_post_request_valid_form(self):
        data = {
            "name": "Test Voting",
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
            "option1": "Option 1",
            "option2": "Option 2",
            "more_options": "Option 3\nOption 4",
        }
        response = self.client.post(reverse("create_classic"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("manage_census"))

        self.assertTrue("voting_id" in self.client.session)
        self.assertIsNotNone(self.client.session["voting_id"])

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Classic voting created successfully!")

    def test_post_request_invalid_form(self):
        data = {
            "name": "",  # Empty name
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
            "option1": "Option 1",
            "option2": "Option 2",
            "more_options": "Option 3\nOption 4",
        }
        response = self.client.post(reverse("create_classic"), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_classic.html")

        form = response.context["form"]

        self.assertFalse(form.is_valid())


class CreateMultipleChoiceViewTest(BaseTestCase):
    def test_get_request(self):
        response = self.client.get(reverse("create_multiple_choice"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_multiple_choice.html")
        self.assertIsInstance(response.context["form"], MultipleChoiceForm)

    def test_post_request_valid_form(self):
        data = {
            "name": "Test Voting",
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
            "option1": "Option 1",
            "option2": "Option 2",
            "more_options": "Option 3\nOption 4",
        }
        response = self.client.post(reverse("create_multiple_choice"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("manage_census"))

        self.assertTrue("voting_id" in self.client.session)
        self.assertIsNotNone(self.client.session["voting_id"])

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Multiple choice voting created successfully!"
        )

    def test_post_request_invalid_form(self):
        data = {
            "name": "",  # Empty name
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
            "option1": "Option 1",
            "option2": "Option 2",
            "more_options": "Option 3\nOption 4",
        }
        response = self.client.post(reverse("create_multiple_choice"), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_multiple_choice.html")

        form = response.context["form"]

        self.assertFalse(form.is_valid())


class CreateOpenQuestionViewTest(BaseTestCase):
    def test_get_request(self):
        response = self.client.get(reverse("create_open_question"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_open_question.html")
        self.assertIsInstance(response.context["form"], OpenQuestionForm)

    def test_post_request_valid_form(self):
        data = {
            "name": "Test Voting",
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
        }
        response = self.client.post(reverse("create_open_question"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("manage_census"))

        self.assertTrue("voting_id" in self.client.session)
        self.assertIsNotNone(self.client.session["voting_id"])

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Open question voting created successfully!")

    def test_post_request_invalid_form(self):
        data = {
            "name": "",  # Empty name
            "desc": "This is a test voting",
            "question_desc": "This is a test question",
        }
        response = self.client.post(reverse("create_open_question"), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "configurator/create_open_question.html")

        form = response.context["form"]

        self.assertFalse(form.is_valid())
