import pickle

# Criar uma lista para armazenar os dados
dataObject = []

# Preencher a lista com valores de 10 a 14 (5 valores)
for num in range(10, 15):
    dataObject.append(num)

# Abrir um arquivo para escrever os dados
file_handler = open('languages', 'wb')

# Serializar e salvar os dados da lista no arquivo usando o módulo pickle
pickle.dump(dataObject, file_handler)

# Fechar o manipulador de arquivo
file_handler.close()

# Abrir o arquivo para leitura
file_handler = open('languages', 'rb')

# Desserializar e carregar os dados do arquivo de volta para a lista
dataObject = pickle.load(file_handler)

# Fechar o manipulador de arquivo
file_handler.close()

# Iterar pela lista e imprimir os valores
for val in dataObject:
    print('Valor dos dados: ', val)
