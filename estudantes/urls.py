from django.urls import path, include
from rest_framework import routers
from estudantes.views import (EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante,
                              ListaMatriculaCurso)

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='estudantes')
router.register('cursos', CursoViewSet, basename='cursos')
router.register('matriculas',MatriculaViewSet,basename='matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view())
]