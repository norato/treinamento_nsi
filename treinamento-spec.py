#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from treinamento import Bola, Quadrado, Retangulo, Pessoa, Televisao, Conta, Bomba, RetanguloCompleto, TrocarCentroRetangulo, Carnivoro, Complexo, NumeroRacional, Numero


class TestBola(unittest.TestCase):

    def setUp(self):
        self.bola = Bola(5, 'preta')

    def test_conferir_tamanho(self):
        self.bola.tamanho |should| equal_to(5)

    def test_conferir_cor(self):
        self.bola.cor |should| equal_to('preta')

    def test_trocar_tamanho(self):
        self.bola.trocar_tamanho(7)
        self.bola.tamanho |should| equal_to(7)

    def test_trocar_cor(self):
        self.bola.trocar_cor('branca')
        self.bola.cor |should| equal_to('branca')


class TestQuadrado(unittest.TestCase):

    def setUp(self):
        self.quadrado = Quadrado(5)

    def test_conferir_lado(self):
        self.quadrado.lado |should| equal_to(5)

    def test_conferir_area(self):
        self.quadrado.area() |should| equal_to(25)

    def test_trocar_lado(self):
        self.quadrado.trocar_lado(7)
        self.quadrado.lado |should| equal_to(7)

    def test_conferir_nova_area(self):
        self.quadrado.trocar_lado(7)
        self.quadrado.area() |should| equal_to(49)


class TestRetangulo(unittest.TestCase):

    def setUp(self):
        self.retangulo = Retangulo(5, 5)

    def test_conferir_altura(self):
        self.retangulo.altura |should| equal_to(5)

    def test_conferir_largura(self):
        self.retangulo.largura |should| equal_to(5)

    def test_conferir_area(self):
        self.retangulo.area() |should| equal_to(25)

    def test_trocar_altura(self):
        self.retangulo.trocar_altura(7)
        self.retangulo.altura |should| equal_to(7)

    def test_trocar_largura(self):
        self.retangulo.trocar_largura(7)
        self.retangulo.largura |should| equal_to(7)

    def test_conferir_perimetro(self):
        self.retangulo.perimetro() |should| equal_to(20)


class TestPessoa(unittest.TestCase):

    def setUp(self):
        self.pessoa = Pessoa(15, 60, 170)

    def test_pessoa_engordar(self):
        self.pessoa.engordar(5)
        self.pessoa.peso |should| equal_to(65)

    def test_pessoa_emagrecer(self):
        self.pessoa.emagrecer(2)
        self.pessoa.peso |should| equal_to(58)

    def test_pessoa_envelhecer_4_anos(self):
        self.pessoa.envelhecer(4)
        self.pessoa.altura |should| equal_to(176)
        self.pessoa.idade |should| equal_to(19)

    def test_pessoa_envelhecer_10_anos(self):
        self.pessoa.envelhecer(10)
        self.pessoa.altura |should| equal_to(179)
        self.pessoa.idade |should| equal_to(25)


class TestTelevisao(unittest.TestCase):

    def setUp(self):
        self.tv = Televisao()

    def test_ligar_tv(self):
        self.tv.ligar()
        self.tv.status |should| equal_to(True)

    def test_trocar_canal_na_faixa(self):
        self.tv.trocar_canal(10)
        self.tv.canal_atual |should| equal_to(10)

    def test_trocar_canal_fora_faixa(self):
        self.tv.trocar_canal(51)
        self.tv.canal_atual |should| equal_to(3)

    def test_trocar_volume_na_faixa(self):
        self.tv.trocar_volume(15)
        self.tv.volume_atual |should| equal_to(15)

    def test_trocar_volume_fora_faixa_maximo(self):
        self.tv.trocar_volume(100)
        self.tv.volume_atual |should| equal_to(30)

    def test_trocar_volume_fora_faixa_minimo(self):
        self.tv.trocar_volume(-100)
        self.tv.volume_atual |should| equal_to(0)

    def test_desligar_tv(self):
        self.tv.desligar()
        self.tv.status |should| equal_to(False)


class TestConta(unittest.TestCase):

    def setUp(self):
        self.conta = Conta(0, 'xunda', 666)

    def test_relatorio(self):
        self.conta.relatorio() |should| equal_to((0, 'xunda', 666))

    def test_deposito(self):
        self.conta.depositar(100)
        self.conta.saldo |should| equal_to(766)

    def test_saque(self):
        self.conta.saque(1000)
        self.conta.saldo |should| equal_to(-334)


class TestBomba_Combustivel(unittest.TestCase):

    def setUp(self):
        self.bomba = Bomba(100, 2)

    def test_consulta_quantidade_combustivel(self):
        self.bomba.capacidade |should| equal_to(100)

    def test_venda_combustivel_por_litro(self):
        self.bomba.venda_litro(30) |should| equal_to(60)
        self.bomba.capacidade |should| equal_to(70)
        self.bomba.venda_litro(80) |should| equal_to('A bomba possui apenas 70 litros')
        self.bomba.capacidade |should| equal_to(70)

    def test_venda_combustivel_por_valor(self):
        self.bomba.venda_valor(60) |should| equal_to(30)
        self.bomba.capacidade |should| equal_to(70)
        self.bomba.venda_valor(1000) |should| equal_to('A bomba possui apenas 70 litros')

    def test_encher_bomba(self):
        self.bomba.venda_litro(30)
        self.bomba.capacidade |should| equal_to(70)
        self.bomba.encher()
        self.bomba.capacidade |should| equal_to(100)

    def test_alterar_preco(self):
        self.bomba.alterar_preco(3)
        self.bomba.preco |should| equal_to(3)


class TestRetanguloCompleto(unittest.TestCase):

    def setUp(self):
        self.retangulo = RetanguloCompleto(10, 12)
        self.ponto_novo = TrocarCentroRetangulo([3, 8])

    def test_trocar_centro(self):
        self.retangulo.centro |should| equal_to([5, 6])
        self.retangulo.centro = self.ponto_novo.ponto
        self.retangulo.centro |should| equal_to([3, 8])

    def test_verificar_vertices(self):
        self.retangulo.vertices |should| equal_to(((0, 0), (0, 10), (12, 0), (12, 10)))

    def test_consultar_ponto(self):
        centro = TrocarCentroRetangulo([4, 7])
        centro.ponto |should| equal_to([4, 7])

    def test_area_retangulo(self):
        self.retangulo.area() |should| equal_to(120)

    def test_perimetro_quadrado(self):
        self.retangulo.perimetro() |should| equal_to(44)

    def test_se_objeto_e_quadrado(self):
        self.retangulo.quadrado() |should| equal_to(False)
        RetanguloCompleto(10, 10, (0, 0)).quadrado() |should| equal_to(True)


class TestCarnivoro(unittest.TestCase):

    def setUp(self):
        self.carnivoro = Carnivoro()
        menu = ['string', False, Pessoa(22, 70, 168).idade, 10]
        for comida in menu:
            self.carnivoro.devorar(comida)

    def test_devorar_tudo_pela_frente(self):
        self.carnivoro.devorar('string')
        self.carnivoro.devorar(False)
        self.carnivoro.devorar(Pessoa(22, 70, 168))
        self.carnivoro.devorar(10)

    def test_ver_o_que_o_bicho_comeu(self):
        self.carnivoro.estomago |should| equal_to(['string', False, 22, 10])

    def test_fazer_digestao(self):
        self.carnivoro.digestao()
        self.carnivoro.estomago |should| equal_to([False, 22, 10])
        self.carnivoro.digestao()
        self.carnivoro.estomago |should| equal_to([22, 10])


class TestCalculadoraComplexos(unittest.TestCase):

    def setUp(self):
        self.numero = Complexo(4, 5)
        self.numero2 = Complexo(3, 7)

    def test_retorna_representacao(self):
        repr(self.numero) |should| equal_to('4 + 5j')

    def test_retornar_parte_real(self):
        self.numero.real |should| equal_to(4)

    def test_retornar_parte_imaginaria(self):
        self.numero.imaginaria |should| equal_to(5)

    def test_soma_numeros(self):
        self.numero + self.numero2 |should| equal_to(Complexo(7, 12))

    def test_subtracao_numeros(self):
        self.numero - self.numero2 |should| equal_to(Complexo(1, -2))

    def test_multiplicacao_numeros(self):
        self.numero * self.numero2 |should| equal_to(Complexo(-23, 43))

    def test_divisao_numeros(self):
        result = self.numero / self.numero2 
        result.real |should| close_to(0.810344827586, delta=0.0000001)
        result.imaginaria |should| close_to(-0.224137931034, delta=0.00000001)


class TestCalculadoraRacional(unittest.TestCase):


    def setUp(self):
        self.numero = NumeroRacional(4,5)
        self.numero2 = NumeroRacional(3,7)
        self.numero3 = NumeroRacional(1,3)

    def test_retornar_numerador(self):
        self.numero.numerador |should| equal_to(4)

    def test_retorna_denominador(self):
        self.numero.denominador |should| equal_to(5)

    def test_retornar_repersentacao(self):
        self.numero.__repr__() |should| equal_to('4/5')

    def test_retornar_ponto_flutuante(self):
        self.numero3.decimal() |should| equal_to(0.33333333333333331)
        self.numero3.decimal(3) |should| equal_to(0.333)
        self.numero3.decimal(5) |should| equal_to(0.33333)

    def test_soma_numero_racional(self):
        self.numero + self.numero2 |should| equal_to(NumeroRacional(43, 35))

    def test_subtracao_numero_racional(self):
        self.numero - self.numero2 |should| equal_to(NumeroRacional(13, 35))

    def test_multiplicacao_numero_racional(self):
        self.numero * self.numero2 |should| equal_to(NumeroRacional(12, 35))

    def test_divisao_numero_racional(self):
        self.numero / self.numero2 |should| equal_to(NumeroRacional(28, 15))


class TestRelatorioNumero(unittest.TestCase):

    def setUp(self):
        self.numero = Numero(4)
        self.numero2 = Numero(10)
        self.numero3 = Numero(7)

    def test_se_numero_par(self):
        self.numero.par_impar() |should| equal_to('par')
        self.numero2.par_impar() |should| equal_to('par')
        self.numero3.par_impar() |should| equal_to('impar')

    def test_retornar_em_romanos(self):
        self.numero.romano() |should| equal_to('IV')
        self.numero2.romano() |should| equal_to('X')
        self.numero3.romano() |should| equal_to('VII')
        Numero(108).romano() |should| equal_to('CVIII')

    def test_termo_fibonacci(self):
        self.numero.fibonacci() |should| equal_to([0 ,1 ,1 ,2])
        self.numero3.fibonacci() |should| equal_to([0, 1, 1, 2, 3, 5, 8])

    def test_fatorial_com_loop(self):
        self.numero.fatorial_loop() |should| equal_to(24)
        self.numero3.fatorial_loop() |should| equal_to(5040)
        Numero(0).fatorial_loop() |should| equal_to(1)

    def test_fatorial_recursivo(self):
        self.numero.fatorial_recursivo() |should| equal_to(24)
        self.numero3.fatorial_recursivo() |should| equal_to(5040)
        Numero(0).fatorial_recursivo() |should| equal_to(1)

    def test_fatorial_funcional(self):
        self.numero.fatorial_funcional() |should| equal_to(24)
        self.numero3.fatorial_funcional() |should| equal_to(5040)
        Numero(0).fatorial_funcional() |should| equal_to(1)
