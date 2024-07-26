from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeListView.as_view(), name = 'recipe-home'),
    path('about/', About, name = 'recipe-about'),
    path('recipe/create/', RecipeCreateView.as_view(), name = 'recipe-create'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'recipe-detail'),
    path('recipe/update/<int:pk>/', RecipeUpdateView.as_view(), name = 'recipe-update'),
    path('recipe/delete/<int:pk>', RecipeDeleteView.as_view(), name = 'recipe-delete'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)