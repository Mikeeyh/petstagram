from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# send_mail(
#     subject="It works",
#     message="It works without HTML",
#     from_email="mikeharalanov@gmail.com",
#     recipient_list=["marayakaneva@gmail.com"],
#     fail_silently=False,
#     # auth_user=None,
#     # auth_password=None,
#     # connection=None,
#     html_message="<h1>It works with HTML!</h1>",
# )
