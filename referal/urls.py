from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
]

# urlpatterns += staticfiles_urlpatterns()
#
# handler404 = pageNotFound
# handler400 = badRequest
# handler403 = forbidden
# handler500 = internalServerError
#
# if settings.DEBUG:
#     urlpatterns += [
#         path("__debug__/", include("debug_toolbar.urls")),
#     ]
