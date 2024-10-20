from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.routers import DefaultRouter
from .views import VerifyOTPView, CustomTokenObtainPairView

from .views import auteur, categorie, commentaire, editeur, emprunt, evaluation, exemplaire, livre

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Appronfondissement backend - API",
      default_version='v1',
      description="Cours appronfissement backend (Django Rest Framework)",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'auteurs', auteur.AuteurViewSet)
router.register(r'categories', categorie.CategorieViewSet)
router.register(r'commentaires', commentaire.CommentaireViewSet)
router.register(r'editeurs', editeur.EditeurViewSet)
router.register(r'emprunts', emprunt.EmpruntViewSet)
router.register(r'evaluations', evaluation.EvaluationViewSet)
router.register(r'exemplaires', exemplaire.ExemplaireViewSet)
router.register(r'livres', livre.LivreViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('/', include(router.urls)),
   path('', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('accounts/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
   path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
