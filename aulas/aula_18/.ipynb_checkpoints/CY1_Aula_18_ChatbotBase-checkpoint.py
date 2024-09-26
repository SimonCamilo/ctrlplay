#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Aula 18
# Novas Funções para Interface Gráfica GUI

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace('Chatbot',nome)

def saudacao_GUI(nome_maquina, nome_usuario):
    import random
    from datetime import datetime, time
    #frases = ['Bom dia! Meu nome é {}. Como vai você?'.format(nome), 'Olá!', 'Oi, tudo bem?']
    #return frases[random.randint(0,2)]
    
    hora_atual = datetime.now().time().hour
    if 0 <= hora_atual < 12:
        return 'Bom dia, {}! Meu nome é {}.'.format(nome_usuario, nome_maquina)
    elif 12 <= hora_atual < 18:
        return 'Boa tarde, {}! Meu nome é {}.'.format(nome_usuario, nome_maquina)
    else:
        return 'Boa noite, {}! Meu nome é {}.'.format(nome_usuario, nome_maquina)

def salva_sugestao(sugestao):
    with open('CY1_Aula_18_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.write('Chatbot: {}\n'.format(sugestao))
        
def buscaResposta_GUI(texto):
    
    palavraProibida = ['bocó','bobo']
    fraseProibida = ['você é horrível','que chatbot insuportável']
    tomMensagem = ['reclamação','elogio','sugestão']
    for p in palavraProibida:
        for frase in fraseProibida:
            if p in texto.strip().lower() or frase in texto.strip().lower():
                return 'Não vem não! Me respeite!'

    for tom in tomMensagem:
        if tom in texto.strip().lower():
            return 'Ok. Você está fazendo um (a) reclamação, elogio ou sugestão'
                
    with open('CY1_Aula_18_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if jaccard(texto, viu) > 0.5:
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
                    
            else:
                conhecimento.write(texto)
                return 'Me desculpe, não sei o que falar'

def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n","Qual","é","sua","favorita","favorito","que","você","acha"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase

