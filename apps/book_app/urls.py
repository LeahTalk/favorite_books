from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^favorites$', views.all_favorites),
    url(r'^add/(?P<book_id>\d+)', views.add_favorite),
    url(r'^edit/(?P<book_id>\d+)', views.edit_book),
    url(r'^delete/(?P<book_id>\d+)', views.delete_book),
    url(r'^removeFavorite/(?P<book_id>\d+)', views.remove_favorite),
    url(r'^(?P<book_id>\d+)', views.book_details),
    url(r'^create_book$', views.create_book),
]
