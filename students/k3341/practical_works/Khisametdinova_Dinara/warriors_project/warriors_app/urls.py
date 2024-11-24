from django.urls import path
from .views import (
    WarriorAPIView,
    ProfessionCreateView,
    SkillListCreateAPIView,
    SkillOfWarriorListCreateAPIView,
    WarriorsWithProfessionsListAPIView,
    WarriorsWithSkillsListAPIView,
    WarriorDetailAPIView,
    WarriorDeleteAPIView,
    WarriorUpdateAPIView,
)


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillListCreateAPIView.as_view(), name='skill-list-create'),
   path('skills-of-warriors/', SkillOfWarriorListCreateAPIView.as_view(), name='skill-of-warrior-list-create'),
   path('warriors/professions/', WarriorsWithProfessionsListAPIView.as_view(), name='warriors-with-professions'),
   path('warriors/skills/', WarriorsWithSkillsListAPIView.as_view(), name='warriors-with-skills'),
   path('warrior/<int:pk>/', WarriorDetailAPIView.as_view(), name='warrior-detail'),
   path('warrior/<int:pk>/delete/', WarriorDeleteAPIView.as_view(), name='warrior-delete'),
   path('warrior/<int:pk>/update/', WarriorUpdateAPIView.as_view(), name='warrior-update'),
]