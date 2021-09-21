class Calculator(object):

    def function(self, func, expr):
        while func in expr:
            pos = expr.index(func)
            res = 0
            if func == "*":
                res = float(expr[pos - 1]) * float(expr[pos + 1])
            elif func == "/":
                res = float(expr[pos - 1]) / float(expr[pos + 1])
            del expr[pos:pos + 2]
            expr[pos - 1] = str(res)
        return expr

    def find_end(self, expr):
        stack = []
        for i in range(len(expr)):
            if expr[i] == "(":
                stack.append(1)
            elif expr[i] == ")" and stack:
                stack.pop()
            elif expr[i] == ")" and not stack:
                return i

    def solve(self, expr):

        while "(" in expr:
            pos = expr.index("(")
            end = self.find_end(expr[pos + 1:])
            res = self.solve(expr[pos + 1:end + pos + 1])
            del expr[pos + 1:end + pos + 2]
            expr[pos] = str(res)

        expr = self.function("/", expr)
        expr = self.function("*", expr)

        i = 0
        while len(expr) != 1:
            if expr[i] == "+":
                res = float(expr[i - 1]) + float(expr[i + 1])
                del expr[i:i + 2]
                expr[i - 1] = str(res)
                i -= 1
            elif expr[i] == "-":
                res = float(expr[i - 1]) - float(expr[i + 1])
                del expr[i:i + 2]
                expr[i - 1] = str(res)
                i -= 1
            i += 1

        return float(expr[0])

    def evaluate(self, formula):
        els = formula.split()
        return self.solve(els)


a = Calculator().evaluate("2 / 2 + 2 * ( 3 + 4 + 8 / ( 2 + 2 ) )")
print(a)
