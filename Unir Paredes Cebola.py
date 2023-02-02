# Desenvolvido por: Prof. Ari Monteiro (Dharma Sistemas)
# Aprenda Dynamo! Acesse: https://www.dharmasistemas.com.br/bim-class-rooms
# Dynamo Insights - União de Paredes Cebola
# Assista a aula no link: https://www.youtube.com/watch?v=Piwtc3Aqilc

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
Camadas = UnwrapElement(IN[0])

# Variável para armazenar resultados
Res = []

# Acessar o documento corrente
Doc = DocumentManager.Instance.CurrentDBDocument

# Iniciar transação para unir camadas
TransactionManager.Instance.EnsureInTransaction(Doc)

# União de camadas
for Camada1, Camada2 in Camadas:
	JoinGeometryUtils.JoinGeometry(Doc, Camada1, Camada2)
	Res.append([Camada1, Camada2])
	
# Finalizar transação para unir camadas
TransactionManager.Instance.TransactionTaskDone()

# Saída
OUT = Res
