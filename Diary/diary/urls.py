
from django.urls import path

from . import views

urlpatterns = [
    path('list/<str:mood>/', views.PostList.as_view(),name='list'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('calendar/',views.calendar,name='calendar'),
    path('profile/', views.detail_profile, name='profile'),
    path('update_profile/', views.update_profile),
    path('item_request',views.item),
    path('delete_post/<int:pk>', views.delete_post),
    # path('save-event/', views.save_event, name='save_event'),
]
