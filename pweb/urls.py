from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from contact.views import HomePageView, ProjectView , download_resume
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home-page'),
    path('contact/',include('contact.urls',namespace='handle-contact')),
    path('projects/',ProjectView.as_view(),name='projects'),
    path('blog/',include('blog.urls',namespace='blog')),
    path('download/', download_resume, name='download-resume'),
    

    # static(settings.STATIC_URL, document.root = settings.STATIC_ROOT)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)