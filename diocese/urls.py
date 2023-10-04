from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CustomUserViewSet, DioceseViewSet, BishopViewSet, ProjectViewSet, ParishViewSet, PriestViewSet, ChapelViewSet, MassScheduleViewSet, YouthGroupViewSet, YouthEventViewSet, DioceseEventViewSet, BlogViewSet, ProfileUpdateView

router = DefaultRouter()
router.register(r'customusers', CustomUserViewSet)
router.register(r'dioceses', DioceseViewSet)
router.register(r'bishops', BishopViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'parishes', ParishViewSet)
router.register(r'priests', PriestViewSet)
router.register(r'chapels', ChapelViewSet)
router.register(r'massschedules', MassScheduleViewSet)
router.register(r'youthgroups', YouthGroupViewSet)
router.register(r'youthevents', YouthEventViewSet)
router.register(r'dioceseevents', DioceseEventViewSet)
router.register(r'blogs', BlogViewSet)


urlpatterns =[
    path('update/', ProfileUpdateView.as_view(), name='profile'),
] + router.urls 