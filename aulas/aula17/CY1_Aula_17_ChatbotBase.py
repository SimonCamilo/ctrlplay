#!/usr/bin/env python
# coding: utf-8

# In[6]:

def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é {}. Como vai você?'.format(nome),
              'Olá!', 'Oi, tudo bem?']
    print(frases[random.randint(0,2)])
    
def recebeTexto(nome):
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibida = ['bocó', 'vagabundo','vagabunda']
    for p in palavraProibida:
        if p in texto:
            print('{}: Não vem não! Me respeite!'.format(nome))
            return recebeTexto(nome)
        return texto

def buscaResposta(nome, texto):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('Cliente: ','') == 'Tchau':
                    print('{}: volte sempre!'.format(nome))
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
            else:
                print('{}: Me desculpe, não sei o que falar'.format(nome))
                conhecimento.write('\n{}'.format(texto))
                resposta_user = input(('{}: O que esperava?\n'.format(nome)))
                conhecimento.write('\nChatbot: {}'.format(resposta_user))
                return 'Hum...'
                
def exibeResposta(resposta, nome):
    print(resposta.replace('Chatbot',nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'

