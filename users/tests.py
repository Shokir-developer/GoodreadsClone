from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser


class RegistrationTestCase(TestCase):
    def test_user_is_created(self):
        self.client.post(reverse("users:register"),
                         data={
                             "username": "shake",
                             "first_name": "Shokir",
                             "last_name": "Begbotov",
                             "email": "begbotovshake@gmail.com",
                             "password": "1111"
                         }
                         )
        user = CustomUser.objects.get(username="shake")
        self.assertEqual(user.first_name, "Shokir")
        self.assertEqual(user.last_name, "Begbotov")
        self.assertEqual(user.email, "begbotovshake@gmail.com")
        self.assertNotEqual(user.password, "1111")
        self.assertTrue(user.check_password("1111"))

    def test_required_fields(self):
        response = self.client.post(reverse("users:register"),
                                    data={
                                        "first_name": "Shokir",
                                        "email": "begbotovshake@gmail.com"
                                    })
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(reverse("users:register"),
                                    data={
                                        "username": "shake",
                                        "first_name": "Shokir",
                                        "last_name": "Begbotov",
                                        "email": "begbotovshake",
                                        "password": "1111"
                                    }
                                    )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = CustomUser.objects.create(username="shake", first_name="Shokir", last_name="Begbotov",
                                         email="begbotovhshake@gmail.com")
        user.set_password("1111")
        user.save()

        response = self.client.post(reverse("users:register"),
                                    data={
                                        "username": "shake",
                                        "first_name": "Shokir2",
                                        "last_name": "Begbotov2",
                                        "email": "begbotovhshake@gmail.com",
                                        "password": "2222"
                                    })
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, "form", "username", "A user with that username already exists.")
