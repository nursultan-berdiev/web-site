from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import IndexView, ItemDetailView, ItemListView, test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('store/', ItemListView.as_view(), name='item_list'),
    path('test/', test, name='test')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
