from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer, UserSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
