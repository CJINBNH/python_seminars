
def logExpr(a):
    with open('file_007.txt', 'w', encoding='utf-8') as f:
        f.write(f'Уравнение: {a} = 0\n')

def logAnswer(b):
    with open('file_007.txt', 'a', encoding='utf-8') as r:
        r.write(f'Корни уравнения: {b}')