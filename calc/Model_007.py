import sympy

def evaluateExpr(expr):
    x = sympy.Symbol('x')
    return str(sympy.solve(expr, x))