from view import Value_type, Get_mode, Print_result, Get_rational_value, Get_complex_value

if Value_type():
    print('Введите первое число') 
    num1 = Get_complex_value() #- ДЛЯ КОМПЛЕКСНЫХ ЧИСЕЛ - ОК
    print('Введите второе число')
    num2 = Get_complex_value()
else:
    print('Введите первое число')  #- ДЛЯ РAЦИОНАЛЬНЫХ ЧИСЕЛ - ОК
    num1 = Get_rational_value()
    print('Введите второе число')
    num2 = Get_rational_value()

operat = Get_mode()
if operat == '+':
    result = num1 + num2
elif operat == '-':
    result = num1 - num2
elif operat == '*':
    result = num1 * num2
elif operat == '/':
    result = num1 / num2

Print_result(operat, num1, num2, result)



