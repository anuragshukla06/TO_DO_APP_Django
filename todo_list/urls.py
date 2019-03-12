from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name = "about"),
    path('delete/<int:item_id>', views.delete, name="delete"),
    path('cross/<int:item_id>', views.cross, name="cross"),
    path('uncross/<int:item_id>', views.uncross, name="uncross"),
    path("edit/<int:item_id>", views.edit, name="edit")
]