from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

"""we import this for jwt token create, refresh, verify"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

"""we create default url which call student api"""
router = DefaultRouter()
router.register("student",views.Studentapi, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    #"when we call curd url it will give as student url by which we can use our api"
    path("curd/", include(router.urls)),
    path("gettoken/", TokenObtainPairView.as_view(), name="token"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verifytoken/", TokenVerifyView.as_view(), name="token_verify"),
]