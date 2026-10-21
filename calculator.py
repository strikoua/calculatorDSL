from textx import metamodel_from_file

class Calculator:
    def factor(self, factor):
        if factor.expression is not None:
            return self.expression(factor.expression)
        else: return factor.number

    def term(self, term):
        num1 = self.factor(term.beginning)
        for oprtr in term.prod:
            num2 = self.factor(oprtr.factor)
            if oprtr.operator == '*':
                num1 = num1 * num2
            elif num2 == 0:
                print("Cannot divide by zero")
                exit()  
            else: num1 = num1 / num2
        return num1

    def expression(self, expr):
        num1 = self.term(expr.beginning)
        for oprtr in expr.sum:
            num2 = self.term(oprtr.term)
            if oprtr.operator == '+':
                num1 = num1 + num2
            else: num1 = num1 - num2
        return num1

    def calculation(self, model):
        print(self.expression(model.expression))


calculator_mm = metamodel_from_file('calculator.tx')
calculator_model = calculator_mm.model_from_file('expression.calc')
calculator = Calculator()
calculator.calculation(calculator_model)                