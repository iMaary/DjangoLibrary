from django.urls import path
from portal.views.homepage import homepage
from portal.views.book.catalog import catalog
from portal.views.book.details import details

urlpatterns = [
    path('', homepage, name='homepage'),
    path('catalog/', catalog, name='catalog'),
    path('book/<int:pk>/', details, name='details'),
]
