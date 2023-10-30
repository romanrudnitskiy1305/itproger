from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('new', views.new, name='new'),
    path('<int:pk>', views.newsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/updata', views.newsUpdata.as_view(), name='news-updata'),
    path('<int:pk>/delete', views.newsDelete.as_view(), name='news-delete')
]
