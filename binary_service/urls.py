"""binary_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework import permissions
from binary.views import document_download_view, document_thumbnail_view


# openapi implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
        title="Binary Data Storage Service",
        default_version='latest',
        description="A service for uploading documents, images and other forms of binary data",
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)              


urlpatterns = [
    path('admin/', admin.site.urls),
        re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    re_path(r'^file/(?P<file_id>\w+)', document_download_view),
    re_path(r'^thumbnail/(?P<file_id>\w+)', document_thumbnail_view),
    path('health_check/', include('health_check.urls')),

]

urlpatterns += staticfiles_urlpatterns()

