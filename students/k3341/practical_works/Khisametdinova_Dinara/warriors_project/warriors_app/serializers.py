from rest_framework import serializers
from .models import *

class WarriorSerializer(serializers.ModelSerializer):

  class Meta:
     model = Warrior
     fields = "__all__"

class ProfessionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"       

class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    class Meta:
        model = SkillOfWarrior
        fields = ["skill", "level"]

class WarriorWithProfessionsSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    skillsofwarrior_set = SkillOfWarriorSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorDetailSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer(many=True)
    skillsofwarrior_set = SkillOfWarriorSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"