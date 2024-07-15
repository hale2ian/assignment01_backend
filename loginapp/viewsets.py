from rest_framework import viewsets

from loginapp.models import ChatRoom
from loginapp.serializers import ChatRoomSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()