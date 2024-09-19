# Desenvolvido por: Prof. Ari Monteiro
# Data: 19-09-2024
# Contato: http://wwww.dharmasistemas.com.br
# Referências:
# https://spiderinnet.typepad.com/blog/2011/04/object-picking-in-revit-api-part-i-pickobject-and-objecttype.html
# https://forum.dynamobim.com/t/is-it-possible-to-prompt-pickpoint-in-revit-from-dynamo/5318


import sys
import clr

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

TaskDialog.Show('Checagem por esferas rolantes', 'Clique um ponto em 2 cabos SPDA')

# Seleção de apenas 2 pontos
outPt = []
for i in range(0, 2):
    picked = uidoc.Selection.PickObject(ObjectType.PointOnElement, 'Clique ponto ' + str(i+1) + ' sobre um cabo SPDA')
    outPt.append(picked.GlobalPoint.ToPoint())

OUT = outPt
