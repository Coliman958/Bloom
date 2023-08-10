from django.urls import path
from . import views
from .views import Homepage, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, AddCategoryView, LikeView, AddCommentView


urlpatterns = [
path('', Homepage.as_view(), name='home'),
path('article_details/<int:pk>', BlogDetailView.as_view(), name='article_details'),
path('add_post', AddPostView.as_view(), name='add_post'),
path('update/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
path('category/<str:cats>/', CategoryView, name='category'),
path('add_category/', AddCategoryView.as_view(), name='add_category'),
path('like/<int:pk>', LikeView, name='like_post'),
path('article_details/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]