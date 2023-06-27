from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test model"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = "test@example.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email normalized"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for input_email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(
                email=input_email,
                password="password123",
            )
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                "",
                "password123",
            )

    def test_new_superuser_successful(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "password123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_superuser_without_email_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                "",
                "password123",
            )
