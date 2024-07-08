from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setup(self) -> None:
        self.make_recipe()
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self, first_name='Author', last_name='Author', username='author', email='L9l3o@example.com', password='123456'):
        return User.objects.create_user(
            first_name=first_name, 
            last_name=last_name, 
            username=username,
            email=email,
            password=password
        )

    def make_recipe(
            self,
            category=None,
            author=None,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-title',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Servings',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
            ):
        if category is None:
            category_data = {}

        if author is None:
            author_data = {}
        
        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published
        )
