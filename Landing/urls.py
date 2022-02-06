from django.urls import path

from .views import HomeViews, DetailsView, CreateViews, DeleteView



urlpatterns = [
    path('',HomeViews, name="HomeViews"),
    path('create/',CreateViews, name="CreateViews"),
    path('<str:id>',DetailsView, name="DetailsView"),
    path('delete/<str:id>/',DeleteView, name="DeleteView")


]
