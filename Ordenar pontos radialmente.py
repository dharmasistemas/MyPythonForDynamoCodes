# Desenvolvido por: Prof. Ari Monteiro (Dharma Sistemas)
# Aprenda Dynamo! Acesse: https://www.dharmasistemas.com.br/bim-class-rooms
# Ordenação de pontos no sentido horário ou anti-horário (ordenação radial)
# Código compatível com o Autodesk Revit 2019

# Carregar as bibliotecas DesignScript e padrão do Python
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

import math


def ObterCentroide(Pontos):
    x, y, z = zip(*[[Pto.X, Pto.Y, Pto.Z] for Pto in Pontos])
    l = len(x)
    c = Point.ByCoordinates(sum(x) / l, sum(y) / l, sum(z) / l)
    return c

# Define a sorting function:
def FuncOrdPto(Pto):
    # Destructure the point to x and y
    x, y = Pto.X, Pto.Y

    # Translate the points according to the estimated center
    x -= Centroide.X
    y -= Centroide.Y

    # Get the angle of this point from the estimated center
    angle = math.atan2(y, x)

    # Get the distance squared of this point from the estimated center
    dist = (x ** 2) + (y ** 2)
    
    return (angle, dist)

# As entradas para este nó serão armazenadas como uma lista nas variáveis IN.
Pontos = IN[0]

# Ordenar pontos radialmente
Centroide = ObterCentroide(Pontos)
PontosOrd = sorted(Pontos, key=FuncOrdPto, reverse=False)

# Retorno
OUT = PontosOrd
