from django.urls import path
from .views import HomeView, ArticleDetailView, AddpostView, BlogEditView,BlogDeleteView
#from . import views

urlpatterns = [
    #path('',views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-view'),
    path('Add_post/', AddpostView.as_view(), name='Add_post'),
    path('article/edit/<int:pk>/', BlogEditView.as_view(), name='update-view'),
    path('article/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete-view'),
]
