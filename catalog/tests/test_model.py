from django.test import TestCase
from catalog.models import Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData:
        # Run once to set up non-modified data for all class methods.

        Author.objects.create(first_name='Big', last_name='Bob')        

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_lable = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_lable, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_lable = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_lable, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_lable = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_lable, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_lable = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_lable, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
