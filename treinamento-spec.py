#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from treinamento import Ball, Square, Rectangle, Person, Television, Account, GasStation, CartesianRectangle,\
                        Point, Carnivorous, Complex, RationalNumber, Number


class TestBall(unittest.TestCase):

    def setUp(self):
        self.ball = Ball(5, 'black')

    def it_check_its_its_size(self):
        self.ball.size |should| equal_to(5)

    def it_check_its_its_collor(self):
        self.ball.collor |should| equal_to('black')

    def it_change_its_size(self):
        self.ball.change_size(7)
        self.ball.size |should| equal_to(7)

    def it_change_its_collor(self):
        self.ball.change_collor('white')
        self.ball.collor |should| equal_to('white')


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(5)

    def it_check_its_its_side(self):
        self.square.side |should| equal_to(5)

    def it_check_its_its_area(self):
        self.square.area() |should| equal_to(25)

    def it_change_side(self):
        self.square.change_side(7)
        self.square.side |should| equal_to(7)

    def it_change_area(self):
        self.square.change_side(7)
        self.square.area() |should| equal_to(49)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 5)

    def it_check_its_height(self):
        self.rectangle.height |should| equal_to(5)

    def it_check_its_width(self):
        self.rectangle.width |should| equal_to(5)

    def it_check_its_area(self):
        self.rectangle.area() |should| equal_to(25)

    def it_change_its_height(self):
        self.rectangle.change_height(7)
        self.rectangle.height |should| equal_to(7)

    def it_change_its_width(self):
        self.rectangle.change_width(7)
        self.rectangle.width |should| equal_to(7)

    def it_check_its_perimeter(self):
        self.rectangle.perimeter() |should| equal_to(20)


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person(15, 60, 170)

    def it_gain_weight(self):
        self.person.gain_weight(5)
        self.person.weight |should| equal_to(65)

    def it_lose_weight(self):
        self.person.lose_weight(2)
        self.person.weight |should| equal_to(58)

    def it_get_old_6_years_and_check_its_height(self):
        self.person.get_old(6)
        self.person.height |should| equal_to(179)
        self.person.old |should| equal_to(21)

    def it_stop_to_get_height_at_21_years(self):
        self.person.get_old(10)
        self.person.height |should| equal_to(179)
        self.person.old |should| equal_to(25)


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def it_turn_on_tv(self):
        self.tv.turn_on_turn_off()
        self.tv.status |should| equal_to(True)

    def it_change_the_channel(self):
        self.tv.change_channel(10)
        self.tv.current_channnel |should| equal_to(10)

    def it_check_if_is_channel_out_of_the_range(self):
        self.tv.change_channel(51)
        self.tv.current_channnel |should| equal_to(3)

    def it_change_the_volume(self):
        self.tv.change_volume(15)
        self.tv.current_volume |should| equal_to(15)

    def it_chack_if_volume_is_above_of_the_range(self):
        self.tv.change_volume(100)
        self.tv.current_volume |should| equal_to(30)

    def it_chack_if_volume_is_below_of_the_range(self):
        self.tv.change_volume(-100)
        self.tv.current_volume |should| equal_to(0)

    def it_turn_off_tv(self):
        self.tv.status = True
        self.tv.turn_on_turn_off()
        self.tv.status |should| equal_to(False)


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(0, 'xunda', 666)

    def it_show_the_statement_account(self):
        self.account.statement() |should| equal_to((0, 'xunda', 666))

    def it_deposit_100_money_in_account(self):
        self.account.deposit(100)
        self.account.balance |should| equal_to(766)

    def it_withdraw_1000_money_off_account(self):
        self.account.withdraw(1000)
        self.account.balance |should| equal_to(-334)


class TestGasStation(unittest.TestCase):

    def setUp(self):
        self.gasstation = GasStation(100, 2)

    def it_verify_the_state_of_the_fuel_pump(self):
        self.gasstation.current_state |should| equal_to(100)

    def it_sell_fuel_by_liter(self):
        self.gasstation.sell_per_liter(30) |should| equal_to(60)
        self.gasstation.current_state |should| equal_to(70)
        self.gasstation.sell_per_liter(80) |should| equal_to('The gasstation only have 70 liters')
        self.gasstation.current_state |should| equal_to(70)

    def it_sell_fuel_by_ammount_value(self):
        self.gasstation.sell_per_value(60) |should| equal_to(30)
        self.gasstation.current_state |should| equal_to(70)
        self.gasstation.sell_per_value(1000) |should| equal_to('The gasstation only have 70 liters')

    def it_supply_gasstation(self):
        self.gasstation.sell_per_liter(30)
        self.gasstation.current_state |should| equal_to(70)
        self.gasstation.supply()
        self.gasstation.current_state |should| equal_to(100)

    def it_change_the_price_per_liter(self):
        self.gasstation.price_per_liter(3)
        self.gasstation.price |should| equal_to(3)


class TestCartesianRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = CartesianRectangle(10, 12)
        self.new_point = Point((3, 8))

    def it_change_its_center(self):
        self.rectangle.center |should| equal_to((5, 6))
        self.rectangle.center = self.new_point.point
        self.rectangle.center |should| equal_to((3, 8))

    def it_check_its_vertices(self):
        self.rectangle.vertices |should| equal_to(((0, 0), (0, 10), (12, 0), (12, 10)))

    def it_check_its_point(self):
        center = Point([4, 7])
        center.point |should| equal_to([4, 7])

    def it_check_its_area(self):
        self.rectangle.area() |should| equal_to(120)

    def it_check_its_perimeter(self):
        self.rectangle.perimeter() |should| equal_to(44)

    def it_if_object_is_a_square(self):
        self.rectangle.square() |should| equal_to(False)
        CartesianRectangle(10, 10).square() |should| equal_to(True)


class TestCarnivorous(unittest.TestCase):

    def setUp(self):
        self.carnivorous = Carnivorous()
        menu = ['string', False, Person(22, 70, 168).old, 10]
        for food in menu:
            self.carnivorous.devour(food)

    def it_devouring_everything_in_its_path(self):
        self.carnivorous.devour('string')
        self.carnivorous.devour(False)
        self.carnivorous.devour(Person(22, 70, 168))
        self.carnivorous.devour(10)

    def it_ascertain_what_the_animal_ate(self):
        self.carnivorous.stomach |should| equal_to(['string', False, 22, 10])

    def it_do_the_digest(self):
        self.carnivorous.digest()
        self.carnivorous.stomach |should| equal_to([False, 22, 10])
        self.carnivorous.digest()
        self.carnivorous.stomach |should| equal_to([22, 10])


class TestComplexCalculator(unittest.TestCase):

    def setUp(self):
        self.number = Complex(4, 5)
        self.number2 = Complex(3, 7)

    def it_returns_the_representation_of_a_complex_number(self):
        repr(self.number) |should| equal_to('4 + 5j')
#        repr(Complex(-3,-5)) |should| equal_to('-3 - 5j')

    def it_returns_the_real_part(self):
        self.number.real |should| equal_to(4)

    def it_returns_the_imaginary_part(self):
        self.number.imaginary |should| equal_to(5)

    def it_sums_complex_numbers(self):
        self.number + self.number2 |should| equal_to(Complex(7, 12))

    def it_subtracts_complex_numbers(self):
        self.number - self.number2 |should| equal_to(Complex(1, -2))

    def test_multiply_complex_numbers(self):
        self.number * self.number2 |should| equal_to(Complex(-23, 43))

    def test_divides_complex_numbers(self):
        result = self.number / self.number2 
        result.real |should| close_to(0.810344827586, delta=0.0000001)
        result.imaginary |should| close_to(-0.224137931034, delta=0.00000001)


class TestRationalCalculator(unittest.TestCase):


    def setUp(self):
        self.number = RationalNumber(4,5)
        self.number2 = RationalNumber(3,7)
        self.number3 = RationalNumber(1,3)

    def it_return_the_numerator(self):
        self.number.numerator |should| equal_to(4)

    def it_returns_the_denominator(self):
        self.number.denominator |should| equal_to(5)

    def it_returns_the_representation(self):
        self.number.__repr__() |should| equal_to('4/5')

    def it_returns_as_floating_point(self):
        self.number3.decimal() |should| equal_to(0.33333333333333331)
        self.number3.decimal(3) |should| equal_to(0.333)
        self.number3.decimal(5) |should| equal_to(0.33333)

    def test_sum_of_rational_numbers(self):
        self.number + self.number2 |should| equal_to(RationalNumber(43, 35))

    def test_substract_of_rational_numbers(self):
        self.number - self.number2 |should| equal_to(RationalNumber(13, 35))

    def test_multiply_of_rational_numbers(self):
        self.number * self.number2 |should| equal_to(RationalNumber(12, 35))

    def test_divisio_of_rational_numbers(self):
        self.number / self.number2 |should| equal_to(RationalNumber(28, 15))


class TestNumberInformation(unittest.TestCase):

    def setUp(self):
        self.number = Number(4)
        self.number2 = Number(10)
        self.number3 = Number(7)

    def test_if_number_is_even_or_odd(self):
        self.number.even_odd() |should| equal_to('even')
        self.number2.even_odd() |should| equal_to('even')
        self.number3.even_odd() |should| equal_to('odd')

    def it_returns_number_in_roman(self):
        self.number.roman() |should| equal_to('IV')
        self.number2.roman() |should| equal_to('X')
        self.number3.roman() |should| equal_to('VII')
        Number(108).roman() |should| equal_to('CVIII')

    def test_term_fibonacci(self):
        self.number.fibonacci() |should| equal_to([0 ,1 ,1 ,2])
        self.number3.fibonacci() |should| equal_to([0, 1, 1, 2, 3, 5, 8])

    def test_looping_factorial(self):
        self.number.looping_factorial() |should| equal_to(24)
        self.number3.looping_factorial() |should| equal_to(5040)
        Number(0).looping_factorial() |should| equal_to(1)

    def test_resursive_factorial(self):
        self.number.resursive_factorial() |should| equal_to(24)
        self.number3.resursive_factorial() |should| equal_to(5040)
        Number(0).resursive_factorial() |should| equal_to(1)

    def test_funcional_factorial(self):
        self.number.funcional_factorial() |should| equal_to(24)
        self.number3.funcional_factorial() |should| equal_to(5040)
        Number(0).funcional_factorial() |should| equal_to(1)
