from datetime import datetime as dt

'''
Функция calc_logger записывает в файл время внесения данных, 
число 1 и число 2 от пользователя 
(вне зависимости от того рациональное оно или нет), 
вид операции над числами и сам результат.
'''
def calc_logger(num1, num2, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}; num1: {};num2: {}; oper: {}; res: {};\n'
                    .format(time, num1, num2, oper, res))