from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.indexView, name="index"),
    path('detect/', views.detectView, name="detect"),
    path('get_video',views.getVideoView, name="get_video")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
