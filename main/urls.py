from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns=[
    path('', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('my_files/', me, name='me'),
    path('my_images/', myImagePage, name='myImage'),
    path('logout/', doLogout, name='logout'),
    path('my_files/add/',addFilesPage, name="addFiles"),
    path('my_files/<int:id>', deleteFilesPage, name="deleteFiles"),
    path('my_images/add/',addImagePage, name="addImage"),
    path('my_images/<int:id>', deleteImagePage, name="deleteImage")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)