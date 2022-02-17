from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# impportacion de modelos

from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ("nombre", "edad")