from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user using email is sucessful"""
        email = 'test@gmail.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test that the new user email is normalized before storing"""
        email = '1singlaaniket@gMail.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='pass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Raise exception if email is not supplied"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password='pass123')

    def test_create_super_user(self):
        """Test create_superuser """
        user = get_user_model().objects.create_superuser(
            'lsjd@gmail.com',
            'pass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
