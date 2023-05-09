from django import views
from rest_framework import viewsets

from .models import EPC
from .serializers import EPCSerializer


class EPCViewSet(viewsets.ModelViewSet):
    queryset = EPC.objects.all()
    serializer_class = EPCSerializer

    def filter_queryset(self, queryset):
        q = super(EPCViewSet, self).filter_queryset(queryset)
        if "postcode" in self.request.query_params:
            q = q.filter(postcode=self.request.query_params["postcode"])
        if "uprn" in self.request.query_params:
            q = q.filter(uprn=self.request.query_params["uprn"])
        return q
