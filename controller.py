from view import Value_type, Get_mode, Print_result, Get_rational_value, Get_complex_value
import modul_sum, modul_sub, modul_div, modul_multi
def calculation():
    num = Value_type()
    if  num== 0:
        Get_rational_value()
        oper = Get_mode()
        if oper == '+':
            modul_sum.summa()
        elif oper == '-':
            modul_sub.sub()
        elif oper == '*':
            modul_multi.Division_real()
        elif oper == '/':
            modul_div.Division_real() 
        Print_result()       


    else:
        Get_complex_value()
        Get_mode()

# operat = Get_mode()
# if operat == '+':
#     result = num1 + num2
# elif operat == '-':
#     result = num1 - num2
# elif operat == '*':
#     result = num1 * num2
# elif operat == '/':
#     result = num1 / num2

# Print_result(operat, num1, num2, result)



