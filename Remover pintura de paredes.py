# Desenvolvido por: Prof. Ari Monteiro (Dharma Sistemas)
# Aprenda Dynamo! Acesse: https://www.dharmasistemas.com.br/bim-class-rooms
# Removendo pintura de paredes (comando "Remover pintura")
# Código compatível com o Autodesk Revit 2019 ou superior

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
Paredes = UnwrapElement(IN[0])

# Variável para armazenar resultados
Res = []

# Acessar o documento corrente
Doc = DocumentManager.Instance.CurrentDBDocument

# Iniciar transação para remover pintura das paredes
TransactionManager.Instance.EnsureInTransaction(Doc)

# Remoção da pintura nas paredes
for Parede in Paredes:
	GeomParede = Parede.get_Geometry(Options())
	GeomObjectEnumerator = GeomParede.GetEnumerator()
	while GeomObjectEnumerator.MoveNext():
		SolidoParede = GeomObjectEnumerator.Current
		if not SolidoParede is None:
			for FaceParede in SolidoParede.Faces:
				if FaceParede.HasRegions:
					for Regiao in FaceParede.GetRegions():
						Doc.RemovePaint(Parede.Id, Regiao)
				else:
					Doc.RemovePaint(Parede.Id, FaceParede)
	
	Res.append(Parede)

# Finalizar transação
TransactionManager.Instance.TransactionTaskDone()

# Saída
OUT = Res
