#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def soma_dos_aninhados(lista):
    soma = 0
    for i in lista:
        if type(i) == list:
            soma += soma_dos_aninhados(i)
        else:
            soma += i 
    return soma

# Teste a sua função aqui (caso ache necessário)

lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

print(soma_dos_aninhados(lista))
print(soma_dos_aninhados(outra_lista))  










