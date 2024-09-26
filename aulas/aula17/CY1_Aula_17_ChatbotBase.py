#!/usr/bin/env python
# coding: utf-8

# In[1]:


def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é {}. como vai voce'.format(nome),
             'ola!', 'oi, tudo bem?']
    print(frases[random.randint(0,2)])

def recebeTexto(nome):
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibida = ["bocó","vagabunda","vagabundo"]
    for p in palavraProibida:
        if p in texto:
            print('{}: não vem não! me respeite!'.format(nome))
            return recebeTexto(nome)
        return texto

def buscaResposta(nome, texto):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as c:
        c.seek(0)
    while True:
        viu = c.readline()
        if viu != '':
            if texto.replace('Cliente: ','') == 'Tchau':
                print('{}: volte sempre!'.format(nome))
                return 'fim'
            elif viu.strip() == texto.strip():
                proximalinha = c.readline()
                if 'Chatbot: ' in  proximalinha:
                    return proximalinha
        else:
            print('{}: Me desculpa, nao sei o que flar'.format(nome))
            c.write('\n{}'.format(texto))
            respostas_user = input(('{}: o queresperava?\n'.format(nome)))
            c.write('n\Chatbot: {}'.format(resposta_user))
            return 'Hum...'

def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == 'fim':
        return "fim"
    return "continua"

