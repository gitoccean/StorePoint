from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('logIn/', views.logIn, name='lgIn'),
    path('signUp/', views.signUp, name='register'),
    path('logOut/', views.logOut, name='lgOut'),
    path('forgotPass/', views.forgotPass, name='forgotPass'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('verify/<auth_token>', views.verify, name="verify"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
