from django.urls import path
from .apiview import *
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings  #include setting form file setting 
from django.conf.urls.static import static #call static in setting


router = DefaultRouter()
router.register('post', PostViewset, base_name='post')
router.register('comment', CommentViewset, base_name='comment')

urlpatterns = [
    path("post/<int:pk>/comment/", CommentList.as_view(), name="post_list"),
    #path("post/<int:pk>/comment/<int:id>/", CommentViewset.as_view({'get':'retrieve'}), name="post_detail"),
    path(r'docs/', include_docs_urls(title='Post API'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls