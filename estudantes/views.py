from estudantes.models import Estudante, Curso, Matricula
from estudantes.serializers import (EstudanteSerializerV1, CursoSerializer, MatriculaSerializer,
                                    ListaMatriculasCursoSerializer,
                                    ListaMatriculasEstudanteSerializer, EstudanteSerializerV2)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from estudantes.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import DjangoModelPermissions


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializerV1


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [DjangoModelPermissions]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [MatriculaAnonRateThrottle, UserRateThrottle]
    #http_method_names = ['get', 'post', ]


class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
