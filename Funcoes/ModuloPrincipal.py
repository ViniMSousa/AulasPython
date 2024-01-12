from Funcoes.IdentificacaoDeFuncoes import *

minhaLista=[]
print("PREENCHENDO")
preencherInventario(minhaLista)
print("EXIBINDO")
exibirInventario(minhaLista)

print("PESQUISANDO")
localizarPorNome(minhaLista)
print("ALTERANDO")
depreciarPorNome(minhaLista, 20)

print("EXCLUINDO")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("RESUMINDO")
resumirValores(minhaLista)