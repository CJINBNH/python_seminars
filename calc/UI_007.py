import Model_007
import Logger_007

def getExpr():      # метод получения информации
    return input()

def showResult(a):  # метод вывода решения уравнения
    print(a)

expression = getExpr() # введение уравнения от пользователя
Logger_007.logExpr(expression) 
answer = Model_007.evaluateExpr(expression) # сохранение результата вычисления
Logger_007.logAnswer(answer)
showResult(answer) # вывод ответа