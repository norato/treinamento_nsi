#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bola(object):

    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.cor = cor

    def trocar_tamanho(self, novo_tamanho):
        self.novo_tamanho = novo_tamanho
        self.tamanho = self.novo_tamanho

    def trocar_cor(self, nova_cor):
        self.nova_cor = nova_cor
        self.cor = self.nova_cor


class Quadrado(object):

    def __init__(self, lado):
        self.lado = lado

    def trocar_lado(self, novo_lado):
        self.novo_lado = novo_lado
        self.lado = self.novo_lado

    def area(self):
        return self.lado * self.lado


class Retangulo(object):

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def trocar_altura(self, nova_altura):
        self.nova_altura = nova_altura
        self.altura = self.nova_altura

    def trocar_largura(self, nova_largura):
        self.nova_largura = nova_largura
        self.largura = self.nova_largura


class Pessoa(object):

    def __init__(self, idade, peso, altura):
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, mais_peso):
        self.mais_peso = mais_peso
        self.peso += self.mais_peso

    def emagrecer(self, menos_peso):
        self.menos_peso = menos_peso
        self.peso -= self.menos_peso

    def envelhecer(self, mais_idade):
        self.mais_idade = mais_idade
        while self.mais_idade != 0:
            if self.idade < 21:
                self.altura += 1.5
            self.idade += 1
            self.mais_idade -= 1


class Televisao(object):

    def __init__(self):
        self.status = False
        self.faixa_canal = (2, 50)
        self.faixa_volume = (0, 30)
        self.canal_atual = 3
        self.volume_atual = 0

    def ligar(self):
        self.status = True

    def trocar_canal(self, canal):
        self.canal = canal
        if self.canal < self.faixa_canal[1] and self.canal > self.faixa_canal[0]:
            self.canal_atual = self.canal

    def trocar_volume(self, volume):
        self.volume = volume
        if self.volume < self.faixa_volume[1] and self.volume > self.faixa_volume[0]:
            self.volume_atual = self.volume
        elif self.volume > self.faixa_volume[1]:
            self.volume_atual = self.faixa_volume[1]
        else: self.volume_atual = self.faixa_volume[0]

    def desligar(self):
        self.status = False


class Conta(object):

    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def relatorio(self):
        return self.numero, self.nome, self.saldo

    def depositar(self, valor):
        self.valor = valor
        self.saldo += self.valor

    def saque(self, valor):
        self.valor = valor
        self.saldo -= self.valor


class Bomba(object):

    def __init__(self, capacidade, preco):
        self.capacidade, self.capacidade_maxima = capacidade, capacidade
        self.preco = preco

    def venda_litro(self, quantidade):
        self.quantidade = quantidade
        if self.quantidade <= self.capacidade:
            self.capacidade -= self.quantidade
            return self.quantidade * self.preco
        return 'A bomba possui apenas %i litros'%(self.capacidade)

    def venda_valor(self, valor):
        self.valor = valor
        quantidade_vendida = self.valor / self.preco
        if quantidade_vendida < self.capacidade:
            self.capacidade -= quantidade_vendida
            return quantidade_vendida
        return 'A bomba possui apenas %i litros'%(self.capacidade)

    def encher(self):
        self.capacidade = self.capacidade_maxima

    def alterar_preco(self, valor):
        self.valor = valor
        self.preco = self.valor


class RetanguloCompleto(object):

    def __init__(self, altura, largura, origem = (0, 0)):
        self.altura = altura
        self.largura = largura
        self.origem = origem
        self.centro = [self.altura / 2 + self.origem[1], self.largura / 2 + self.origem[0]]
        self.vertices = ((self.origem[1], self.origem[0]), (self.origem[1], self.altura + self.origem[0]), \
                         (self.largura + self.origem[1], self.origem[0]), (self.largura + self.origem[1], self.altura + self.origem[0]))

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def quadrado(self):
        return self.largura == self.altura and True or False


class TrocarCentroRetangulo(object):

    def __init__(self, ponto):
        self.ponto = ponto


class Carnivoro(object):

    def __init__(self):
        self.estomago = []

    def devorar(self, alimento):
        self.alimento = alimento
        self.estomago.append(self.alimento)

    def digestao(self):
        self.estomago.pop(0)


class Complexo(object):

    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def __repr__(self):
        return ('%s + %sj') % (self.real, self.imaginaria)

    def __eq__(self, other):
        return self.real == other.real and self.imaginaria == other.imaginaria

    def __add__(self, other):
        soma_real = self.real + other.real
        soma_imaginaria = self.imaginaria + other.imaginaria
        return Complexo(soma_real, soma_imaginaria)

    def __sub__(self, other):
        sub_real = self.real - other.real
        sub_imagirio = self.imaginaria - other.imaginaria
        return Complexo(sub_real, sub_imagirio)

    def __mul__(self, other):
        mul_real = (self.real * other.real - self.imaginaria * other.imaginaria)
        mul_imaginaria = (self.imaginaria * other.real + self.real * other.imaginaria)
        return Complexo(mul_real, mul_imaginaria)

    def __div__(self, other):
        div_real = ((self.real * other.real + self.imaginaria * other.imaginaria) / float(other.real ** 2 + other.imaginaria ** 2))
        div_imaginaria = ((self.imaginaria * other.real - self.real * other.imaginaria) / float(other.real ** 2 + other.imaginaria ** 2))
        return (Complexo(div_real, div_imaginaria))


class NumeroRacional(object):


    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        return ('%s/%s')%(self.numerador, self.denominador)

    def __eq__(self, other):
        return self.numerador == other.numerador and self.denominador == other.denominador

    def __add__(self, other):
        soma_numerador = (self.numerador * other.denominador + self.denominador * other.numerador)
        soma_denominador = (self.denominador * other.denominador)
        return NumeroRacional(soma_numerador, soma_denominador)

    def __sub__(self, other):
        sub_numerador = (self.numerador * other.denominador - self.denominador * other.numerador)
        sub_denominador = (self.denominador * other.denominador)
        return NumeroRacional(sub_numerador, sub_denominador)

    def __mul__(self, other):
        mul_numerador = (self.numerador * other.numerador)
        mul_denominador = (self.denominador * other.denominador)
        return NumeroRacional(mul_numerador, mul_denominador)

    def __div__(self, other):
        mul_numerador = (self.numerador * other.denominador)
        mul_denominador = (self.denominador * other.numerador)
        return NumeroRacional(mul_numerador, mul_denominador)

    def decimal(self, casa=0):
        self.casa = casa
        if self.casa == 0:
            return float(self.numerador) / self.denominador
        return round(float(self.numerador) / self.denominador, self.casa )


class Numero(object):

    def __init__(self, valor):
        self.valor = valor

    def par_impar(self):
        return self.valor % 2 == 0 and 'par' or 'impar'

    def romano(self):
        return Numero((self.valor) / 1000)._convert('M', '', '') + Numero((self.valor % 1000) / 100)._convert( 'C', 'D', 'M') + \
                Numero((self.valor % 100) /10)._convert( 'X', 'L', 'C') + Numero(self.valor % 10)._convert('I', 'V', 'X')

    def _convert(self, um, cinco, dez):
        if 1 <= self.valor <= 3: 
            return um * self.valor
        if self.valor == 4: 
            return um + cinco
        if 5 <= self.valor <= 8: 
            return cinco + um * (self.valor - 5)
        if self.valor == 9: 
            return um + dez
        return ''

    def fibonacci(self):
        resposta = []
        if self.valor in (0,1,2):
            return [1] * self.valor
        resposta = [0, 1]
        for n in range(2, self.valor):
            resposta.append(resposta[n-1] + resposta[ n-2])
        return resposta

    def fatorial_loop(self):
        resposta = 1
        for fator in range(1, self.valor+1):
            resposta *= fator
        return resposta

    def fatorial_recursivo(self):
        if self.valor == 0:
            return 1
        return self.valor * Numero(self.valor - 1).fatorial_recursivo()

    def fatorial_funcional(self):
        return reduce(lambda x,y: x*y, range(1, self.valor+1) or [1])

