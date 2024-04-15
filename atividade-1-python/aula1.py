def contarPalavras(lista):
    contaLetras = 0
    contaPalavras = 0
    
    for palavras in lista:
        contaPalavras += 1
        for _ in palavras:
            contaLetras += 1
        print('Palavra ', '[', palavras, ']', ' contém ', contaLetras, ' letras')
        contaLetras = 0
    print('Total de palavras ', contaPalavras)
            
listaDePalavras = ['oi', 'Sarah', 'tudo bem?']
contarPalavras(listaDePalavras)