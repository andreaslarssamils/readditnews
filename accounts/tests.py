from allauth.account.views import SignupView
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse


class CustomUserTests(TestCase):
    """Tests for the custom user model."""

    def test_create_user(self):
        """Test creating a regular user with the custom user model."""
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="testuser@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser with the custom user model."""

        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    """Tests for the signup page view and form."""

    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        """Set up the test client and get the signup page."""
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        """Test that the signup page uses the correct template and contains the expected content."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Create an account")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        """Test that the signup form works correctly."""
        response = self.client.post(
            reverse("account_signup"),
            {
                "username": self.username,
                "email": self.email,
                "password1": "testpass123!",
                "password2": "testpass123!",
            },
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for a redirect after successful signup
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    def test_signup_view(self):
        """Test that the signup URL resolves to the correct view."""
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)
