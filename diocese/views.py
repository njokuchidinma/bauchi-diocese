from rest_framework import viewsets, generics
from .models import CustomUser, Diocese, Bishop, Project, Parish, Priest, Chapel, MassSchedule, YouthGroup, YouthEvent, Diocese_Event, Blog
from .serializers import CustomUserSerializer, DioceseSerializer, BishopSerializer, ProjectSerializer, ParishSerializer, PriestSerializer, ChapelSerializer, MassScheduleSerializer, YouthGroupSerializer, YouthEventSerializer, DioceseEventSerializer, BlogSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class DioceseViewSet(viewsets.ModelViewSet):
    queryset = Diocese.objects.all()
    serializer_class = DioceseSerializer
    permission_classes = [IsAdminUser]

class BishopViewSet(viewsets.ModelViewSet):
    queryset = Bishop.objects.all()
    serializer_class = BishopSerializer
    permission_classes = [IsAdminUser]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ParishViewSet(viewsets.ModelViewSet):
    queryset = Parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [IsAdminUser]

class PriestViewSet(viewsets.ModelViewSet):
    queryset = Priest.objects.all()
    serializer_class = PriestSerializer
    permission_classes = [IsAdminUser]

class ChapelViewSet(viewsets.ModelViewSet):
    queryset = Chapel.objects.all()
    serializer_class = ChapelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MassScheduleViewSet(viewsets.ModelViewSet):
    queryset = MassSchedule.objects.all()
    serializer_class = MassScheduleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class YouthGroupViewSet(viewsets.ModelViewSet):
    queryset = YouthGroup.objects.all()
    serializer_class = YouthGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class YouthEventViewSet(viewsets.ModelViewSet):
    queryset = YouthEvent.objects.all()
    serializer_class = YouthEventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DioceseEventViewSet(viewsets.ModelViewSet):
    queryset = Diocese_Event.objects.all()
    serializer_class = DioceseEventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProfileUpdateView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
