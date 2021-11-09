# OBTER PRIMEIRO DÍGITO
def primeiroDigito(cpf):
    multiplicador = 10
    soma = 0
    for n in cpf[:9]:
        produto = multiplicador*int(n)
        multiplicador -= 1
        soma += produto
    return divisao(soma)

def divisao(soma):
    resultado = 11 - (soma % 11)
    if resultado > 9:
        digito = 0
        return digito
    else:
        digito = resultado
        return digito

# OBTER SEGUNDO DÍGITO

def segundoDigito(cpf):
    multiplicador = 11
    soma = 0
    for n in cpf[:10]:
        produto = multiplicador*int(n)
        multiplicador -= 1
        soma += produto
    return divisao(soma)

def testeNumerosIguais(cpf):
    for n in cpf:
        if n == cpf[0]:
            continue
        else:
            return primeiroDigito(cpf)
            break
    return 0

def validador(cpf):
    if len(cpf) != 11:
        return f'CPF inválido'
    if testeNumerosIguais(cpf) == 0:
        return f'CPF inválido'

    digito1 = primeiroDigito(cpf)
    print(digito1)
    digito2 = segundoDigito(cpf)
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return f'CPF válido'
    else:
        return f'CPF inválido passou aqui'



if __name__ == '__main__':
    cpf = input('Digite o cpf: ')
    print(validador(cpf))

