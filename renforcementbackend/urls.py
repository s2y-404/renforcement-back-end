from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.routers import DefaultRouter

from .views import auteur, categorie, commentaire, editeur, emprunt, evaluation, exemplaire, livre, user

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
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
   path('api/', include(router.urls)),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
   path('api/user/', user.UserViewSet.as_view(), name='user'),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
