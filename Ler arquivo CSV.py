# Desenvolvido por: Prof. Ari Monteiro
# Data: 04-12-2023
# Contato: http://wwww.dharmasistemas.com.br
# Referências:
# https://stackoverflow.com/questions/6726953/open-the-file-in-universal-newline-mode-using-the-csv-django-module
# https://www.geeksforgeeks.org/reading-rows-from-a-csv-file-in-python/

# Importação da biblioteca de módulos do IronPython 2.7
import sys
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')

# Importação da biblioteca para trabalhar com arquivos CSV
import csv

# Entradas
ArquivoCSV = IN[0]
Delimitador = IN[1]

Res = []

# Ler dados no arquivo CSV
with open(ArquivoCSV,'rU') as file:
	# Ponteiro de arquivo
	readerFile = csv.reader(file, delimiter = Delimitador, lineterminator='\r')
	
	# Ler as linhas do arquivo
	for row in readerFile:
		Res.append(row)

# Atribua a sua saída para a variável OUT.
OUT = Res
