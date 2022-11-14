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
    a + bi
    '''
    print('Введите комплексное число в сл. формате: a + bi')
    print('Например: 24 + 5i\n')
    value = input()
    return value

def Get_Rational_Part(value):
    ''' 
    Получение рациональной части введенного комплексного числа
    '''
    rational_part = []
    for i in range(0, len(value)):
        if value[i] != ' ':
            rational_part.append(value[i])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part

def Get_Imaginary_Part(value):
    ''' 
    Получение 'мнимой единицы' введенного комплексного числа
    '''
    imaginary_part = []
    for i in range(0, len(value)):
        if value[i] == 'i':
            while value[i] != ' ':
                imaginary_part.insert(0,value[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def Get_Symbol(value):
    ''' 
    Возврашает - или - между рациональной и мнимой частью введенного комплексного числа
    '''
    symbol = []
    for l in range(0, len(value)):
        if value[l] == '-' and l !=0 or value[l] == '+' and l != 0:
            symbol.append(value[l])
    symbol = ''.join(symbol)
    return symbol

# print('Введите первое число')  #- ДЛЯ РAЦИОНАЛЬНЫХ ЧИСЕЛ - ОК
# num1 = get_rational_value()
# print('Введите второе число')
# num2 = get_rational_value()
# resul = num1 + num2
# operat = get_mode()
# print(return_result(resul, operat))

# my_compl_val = Get_complex_value() #- ДЛЯ КОМПЛЕКСНЫХ ЧИСЕЛ - ОК
# rational_part = Get_Rational_Part(my_compl_val)
# symbol = Get_Symbol(my_compl_val)
# imagin_part = Get_Imaginary_Part(my_compl_val)
# print(f'{rational_part} {symbol} {imagin_part}i')
