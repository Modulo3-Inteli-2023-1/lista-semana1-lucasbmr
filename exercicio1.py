#  Se achar necessario, faça import de outras bibliotecas



# Crie a função que será avaliada no exercício aqui

def multiplas_operacos(a,b):
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

print(multiplas_operacos(10,2))









