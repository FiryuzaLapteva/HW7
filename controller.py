from view import Value_type, Get_mode, Print_result, Get_rational_value, Get_complex_value
from logger import calc_logger
import modul_sum, modul_div, modul_multi, modul_sub

def Launch_project():
    if Value_type():
        print('Введите первое число') 
        num1 = Get_complex_value() #- ДЛЯ КОМПЛЕКСНЫХ ЧИСЕЛ - ОК
        print('Введите второе число')
        num2 = Get_complex_value()
        operat = Get_mode()
        if operat == '+':
            result = modul_sum.summa(num1, num2)
        elif operat == '-':
            result = modul_sub.sub(num1, num2)
        elif operat == '*':
            result = modul_multi.Mult(num1, num2)
        elif operat == '/':
            result = modul_div.Division(num1, num2)
    else:
        print('Введите первое число')  #- ДЛЯ РAЦИОНАЛЬНЫХ ЧИСЕЛ - ОК
        num1 = Get_rational_value()
        print('Введите второе число')
        num2 = Get_rational_value()
        operat = Get_mode()
        if operat == '+':
            result = modul_sum.summa_compl(num1, num2)
        elif operat == '-':
            result = modul_sub.sub_compl(num1, num2)
        elif operat == '*':
            result = modul_multi.Mult_compl(num1, num2)
        elif operat == '/':
            result = modul_div.Division_compl(num1, num2)
    calc_logger(num1, num2, operat, result)

    Print_result(operat, num1, num2, result)



