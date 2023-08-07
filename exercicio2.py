#  Se achar necessario, faça import de outras bibliotecas

##Lucas Bittencourt Moraes Rego Turma 9



# Crie a função que será avaliada no exercício aqui

def cumulativo(lista):
    soma = 0 
    lista_cumulativa = []
    
    for num in lista:
        soma += num
        lista_cumulativa.append(soma)
    
    return lista_cumulativa


# Teste a sua função aqui (caso ache necessário)

lista = [2,3,4,5]
print(cumulativo(lista))










