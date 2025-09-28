# dishes/tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import date, time
from .models import Category, Dishes, Drink, Reservation
from .forms import ReservationForm

class ModelTests(TestCase):
    """Test cases for models"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
    
    def test_category_creation(self):
        """Test category model creation"""
        category = Category.objects.create(name='Main Course')
        self.assertEqual(str(category), 'Main Course')
        self.assertEqual(category.name, 'Main Course')
    
    def test_dish_creation(self):
        """Test dish model creation"""
        dish = Dishes.objects.create(
            title='Test Dish',
            slug='test-dish',
            author=self.user,
            category=self.category,
            description='A test dish',
            price=15.99,
            status=1
        )
        self.assertEqual(str(dish), 'Test Dish')
        self.assertEqual(dish.price, 15.99)
        self.assertEqual(dish.status, 1)  # Published
    
    def test_reservation_creation(self):
        """Test reservation model creation"""
        reservation = Reservation.objects.create(
            name='John Doe',
            email='john@example.com',
            guests=4,
            date=date.today(),
            time=time(19, 30),
            status=0
        )
        self.assertEqual(str(reservation), f'John Doe - {date.today()} at 19:30:00')
        self.assertEqual(reservation.guests, 4)
        self.assertEqual(reservation.status, 0)  # Pending

class FormTests(TestCase):
    """Test cases for forms"""
    
    def test_reservation_form_valid(self):
        """Test valid reservation form"""
        form_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'guests': 2,
            'date': date.today(),
            'time': time(20, 0)
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_reservation_form_invalid_guests(self):
        """Test reservation form with invalid guest count"""
        form_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'guests': 0,  # Invalid: less than 1
            'date': date.today(),
            'time': time(20, 0)
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors)

class ViewTests(TestCase):
    """Test cases for views"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        self.dish = Dishes.objects.create(
            title='Test Dish',
            slug='test-dish',
            author=self.user,
            category=self.category,
            description='A test dish',
            price=15.99,
            status=1
        )
    
    def test_homepage_view(self):
        """Test homepage loads correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Cameroonian Table')
        self.assertContains(response, 'Test Dish')
    
    def test_reservation_form_submission(self):
        """Test reservation form submission"""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'guests': 4,
            'date': date.today(),
            'time': time(19, 30)
        }
        response = self.client.post(reverse('home'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Reservation.objects.filter(name='John Doe').exists())