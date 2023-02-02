# Desenvolvido por: Prof. Ari Monteiro (Dharma Sistemas)
# Aprenda Dynamo! Acesse: https://www.dharmasistemas.com.br/bim-class-rooms
# Alterando as unidades de comprimento e área do projeto
# Código compatível com o Autodesk Revit 2019

# Importação da biblioteca de programação do Revit
import clr

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Entradas
dataEnteringNode = IN

# Acessar o documento corrente
Doc = DocumentManager.Instance.CurrentDBDocument

# Acessando as unidades do documento corrente
Unidades = Doc.GetUnits()

# Definindo a unidade de comprimento: metros com 2 casas de precisão
TipoUnidComp = UnitType.UT_Length
FormUnidComp = FormatOptions(DisplayUnitType.DUT_METERS, 0.01)
Unidades.SetFormatOptions(TipoUnidComp, FormUnidComp)

# Definindo a unidade de área: metros quadrados com 2 casas de precisão
TipoUnidArea = UnitType.UT_Area
FormUnidArea = FormatOptions(DisplayUnitType.DUT_SQUARE_METERS, 0.01)
Unidades.SetFormatOptions(TipoUnidArea, FormUnidArea)

# Iniciar transação para ajustar as unidades do projeto
TransactionManager.Instance.EnsureInTransaction(Doc)

# Ajustando as unidades do projeto
Doc.SetUnits(Unidades)

# Finalizar transação
TransactionManager.Instance.TransactionTaskDone()

# Saída
OUT = "Unidades alteradas. Cheque o comando Units!"
