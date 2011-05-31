#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ball(object):

    def __init__(self, size, collor):
        self.size = size
        self.collor = collor

    def change_size(self, new_size):
        self.new_size = new_size
        self.size = self.new_size

    def change_collor(self, new_collor):
        self.new_collor = new_collor
        self.collor = self.new_collor


class Square(object):

    def __init__(self, side):
        self.side = side

    def change_side(self, new_side):
        self.new_side = new_side
        self.side = self.new_side

    def area(self):
        return pow(self.side, 2) 


class Rectangle(object):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def change_height(self, new_height):
        self.new_height = new_height
        self.height = self.new_height

    def change_width(self, new_width):
        self.new_width = new_width
        self.width = self.new_width


class Person(object):

    def __init__(self, old, weight, height):
        self.old = old
        self.weight = weight
        self.height = height

    def gain_weight(self, get_weight):
        self.get_weight = get_weight
        self.weight += self.get_weight

    def lose_weight(self, lose_weight):
        self.lose_weight = lose_weight
        self.weight -= self.lose_weight

    def get_old(self, get_old):
        self.get_old = get_old
        while self.get_old != 0:
            if self.old < 21:
                self.height += 1.5
            self.old += 1
            self.get_old -= 1


class Television(object):


    def __init__(self):
        self.status = False
        self.channel_range = (2, 50)
        self.volume_range = (0, 30)
        self.current_channnel = 3
        self.current_volume = 0

    def turn_on_turn_off(self):
        if self.status == False:
            self.status = True
        else: self.status = False


    def change_channel(self, channel):
        self.channel = channel
        if self.channel < self.channel_range[1] and self.channel > self.channel_range[0]:
            self.current_channnel = self.channel

    def change_volume(self, volume):
        self.volume = volume
        if self.volume < self.volume_range[1] and self.volume > self.volume_range[0]:
            self.current_volume = self.volume
        elif self.volume > self.volume_range[1]:
            self.current_volume = self.volume_range[1]
        else: self.current_volume = self.volume_range[0]


class Account(object):

    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def statement(self):
        return self.number, self.name, self.balance

    def deposit(self, value):
        self.value = value
        self.balance += self.value

    def withdraw(self, value):
        self.value = value
        self.balance -= self.value


class GasStation(object):

    def __init__(self, current_state, price):
        self.current_state, self.maximum_capacicy = current_state, current_state
        self.price = price

    def sell_per_liter(self, amount):
        self.amount = amount
        if self.amount <= self.current_state:
            self.current_state -= self.amount
            return self.amount * self.price
        return 'The gasstation only have %i liters' % (self.current_state)

    def sell_per_value(self, value):
        self.value = value
        sold = self.value / self.price
        if sold < self.current_state:
            self.current_state -= sold
            return sold
        return 'The gasstation only have %i liters' % (self.current_state)

    def supply(self):
        self.current_state = self.maximum_capacicy

    def price_per_liter(self, value):
        self.value = value
        self.price = self.value


class CartesianRectangle(Rectangle):


    def __init__(self, height, width, point = (0, 0)):
        super(CartesianRectangle, self).__init__(height, width)
        self.center = (self.height / 2, self.width / 2)
        self.vertices = ((0, 0), (0, self.height ),(self.width, 0), (self.width  , self.height ))

    def square(self):
        return self.width == self.height and True or False


class Point(object):

    def __init__(self, point, origin = (0,0)):
        self.point = point

class Carnivorous(object):

    def __init__(self):
        self.stomach = []

    def devour(self, food):
        self.food = food
        self.stomach.append(self.food)

    def digest(self):
        self.stomach.pop(0)


class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return ('%s + %sj') % (self.real, self.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        sum_real = self.real + other.real
        sum_imaginary = self.imaginary + other.imaginary
        return Complex(sum_real, sum_imaginary)

    def __sub__(self, other):
        sub_real = self.real - other.real
        sub_imagirio = self.imaginary - other.imaginary
        return Complex(sub_real, sub_imagirio)

    def __mul__(self, other):
        mul_real = (self.real * other.real - self.imaginary * other.imaginary)
        mul_imaginary = (self.imaginary * other.real + self.real * other.imaginary)
        return Complex(mul_real, mul_imaginary)

    def __div__(self, other):
        div_real = ((self.real * other.real + self.imaginary * other.imaginary) / float(other.real ** 2 + other.imaginary ** 2))
        div_imaginary = ((self.imaginary * other.real - self.real * other.imaginary) / float(other.real ** 2 + other.imaginary ** 2))
        return (Complex(div_real, div_imaginary))


class RationalNumber(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return ('%s/%s') % (self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __add__(self, other):
        sum_numerator = (self.numerator * other.denominator + self.denominator * other.numerator)
        sum_denominator = (self.denominator * other.denominator)
        return RationalNumber(sum_numerator, sum_denominator)

    def __sub__(self, other):
        sub_numerator = (self.numerator * other.denominator - self.denominator * other.numerator)
        sub_denominator = (self.denominator * other.denominator)
        return RationalNumber(sub_numerator, sub_denominator)

    def __mul__(self, other):
        mul_numerator = (self.numerator * other.numerator)
        mul_denominator = (self.denominator * other.denominator)
        return RationalNumber(mul_numerator, mul_denominator)

    def __div__(self, other):
        mul_numerator = (self.numerator * other.denominator)
        mul_denominator = (self.denominator * other.numerator)
        return RationalNumber(mul_numerator, mul_denominator)

    def decimal(self, _decimal = 0):
        self._decimal = _decimal
        if self._decimal == 0:
            return float(self.numerator) / self.denominator
        return round(float(self.numerator) / self.denominator, self._decimal)


class Number(object):

    def __init__(self, value):
        self.value = value

    def even_odd(self):
        return self.value % 2 == 0 and 'even' or 'odd'

    def roman(self):
        return Number((self.value) / 1000)._convert('M', '', '') + Number((self.value % 1000) / 100)._convert('C', 'D', 'M') + \
                Number((self.value % 100) /10)._convert('X', 'L', 'C') + Number(self.value % 10)._convert('I', 'V', 'X')

    def _convert(self, one, five, ten):
        if 1 <= self.value <= 3:
            return one * self.value
        if self.value == 4:
            return one + five
        if 5 <= self.value <= 8:
            return five + one * (self.value -5)
        if self.value == 9:
            return one + ten
        return ''

    def fibonacci(self):
        result = []
        if self.value in (0, 1, 2):
            return [1] * self.value
        result = [0, 1]
        for n in range(2, self.value):
            result.append(result[n -1] + result[n -2])
        return result

    def looping_factorial(self):
        result = 1
        for fator in range(1, self.value + 1):
            result *= fator
        return result

    def resursive_factorial(self):
        if self.value == 0:
            return 1
        return self.value * Number(self.value -1).resursive_factorial()

    def funcional_factorial(self):
        return reduce(lambda x, y: x * y, range(1, self.value + 1) or [1])
