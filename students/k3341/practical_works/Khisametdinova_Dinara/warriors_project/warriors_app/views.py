from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *

class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})
   
class ProfessionCreateView(APIView):

    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionCreateSerializer(professions, many=True)
        return Response({"Professions": serializer.data})
   
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)
        if serializer.is_valid(raise_exception=True):
           profession_saved = serializer.save()
        return Response({"Success": f"Profession '{profession_saved.title}' created successfully."})
    
class SkillListCreateAPIView(APIView):
   
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
       
class SkillOfWarriorListCreateAPIView(APIView):
    
    def get(self, request):
        skills_of_warriors = SkillOfWarrior.objects.all()
        serializer = SkillOfWarriorSerializer(skills_of_warriors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillOfWarriorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WarriorsWithProfessionsListAPIView(generics.ListAPIView):
    serializer_class = WarriorWithProfessionsSerializer
    queryset = Warrior.objects.all()

class WarriorsWithSkillsListAPIView(generics.ListAPIView):
    serializer_class = WarriorWithSkillsSerializer
    queryset = Warrior.objects.all()

class WarriorDetailAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorDetailSerializer
    queryset = Warrior.objects.all()

class WarriorDeleteAPIView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()

class WarriorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

