def Value_type():
    ''' 
    Ввод типа чисел
    0 - рациональное
    1 - комплексное
    '''
    type = int(input('Введите "0", если будем производить вычисления с рациональными числами, или "1" - если с комплексными '))
    if type == 0 or type == 1:
        return type
    else:
        print('Вы некорректно ввели тип чисел. Используйте символы 0 или 1')

def Get_mode():
    ''' 
    Ввод операции (+ - * /)
    '''
    mode = input('Введите интересующую вас операцию соответствующим символом: + сложение, - вычитание, * умножение, / деление  ')
    if mode in ['+', '-', '*', '/']:
        return mode
    else:
        print('Вы некорректно ввели опереацию. Используйте символы + - * /')

#Библиотека операций    
mode = {'+': 'сложения', '-': 'вычитания', '*': 'умножения', '/': 'деления'}

def Return_result(res, oper):
    ''' 
    Вывод результата расчета
    '''
    return f'Результат операции {mode[oper]} = {res}'

def Get_rational_value():
    ''' 
    Ввод рационального числа
    '''
    value = float(input())
    return value

def Get_complex_value():
    ''' 
    Ввод комплексного числа в формате
    'a+bi'
    '''
    print('Введите комплексное число в сл. формате: a+bi. Без пробелов')
    print('Например: 2+1j')
    value = complex(input())
    return value

# print('Введите первое число')  #- ДЛЯ РAЦИОНАЛЬНЫХ ЧИСЕЛ - ОК
# num1 = get_rational_value()
# print('Введите второе число')
# num2 = get_rational_value()
# resul = num1 + num2
# operat = get_mode()
# print(return_result(resul, operat))

# my_compl_val1 = Get_complex_value() #- ДЛЯ КОМПЛЕКСНЫХ ЧИСЕЛ - ОК
# print(my_compl_val1)
# print(type(my_compl_val1))
# my_compl_val2 = Get_complex_value()
# print(f'"SUM = {my_compl_val1 + my_compl_val2}')


