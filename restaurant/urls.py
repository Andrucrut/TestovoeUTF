from django.urls import path

from restaurant import views

urlpatterns = [
    path('api/v1/foods/', views.FoodCategories.as_view(), name='food_categories'),

]