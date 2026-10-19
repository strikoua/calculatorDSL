from textx import metamodel_from_file

class Calculator:
    def calculate(self, model):
        num1 = 0
        num2 = 0
        operator = 'empty'
        for b in model.buttons:
            if b.__class__.__name__ == 'NumberButton':
                if operator == 'empty':
                    num1 = b.num
                else:
                    num2 = b.num
                    match operator:
                        case '+': num1 = num1 + num2
                        case '-': num1 = num1 - num2
                        case '*': num1 = num1 * num2
                        case '/': num1 = num1 / num2 #add result if num2 = 0
            else:
                operator = b.operation
        print(num1)

calculator_mm = metamodel_from_file('calculator.tx')
calculator_model = calculator_mm.model_from_file('expression.rbt')
calculator = Calculator()
calculator.calculate(calculator_model)                