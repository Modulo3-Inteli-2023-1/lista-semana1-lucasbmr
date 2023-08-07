#  Se achar necessario, faça import de outras bibliotecas

##Lucas Bittencourt Moraes Rego Turma 9


# Crie a função que será avaliada no exercício aqui

def multiplas_operacoes(a,b):
    soma = a + b
    sub = a - b 
    mult = a * b
    
    ## evitar divisão por 0
    if b == 0:
        div = 0
    else:
        div = a / b
        
    return soma , sub , mult, div 
    

# Teste a sua função aqui (caso ache necessário)

print(multiplas_operacoes(10,2))









