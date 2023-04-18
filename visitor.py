from kmmszarp.kmmszarpVisitor import kmmszarpVisitor as baseVisitor
from kmmszarp.kmmszarpParser import kmmszarpParser
from err import ExecutionError, VariableNotDeclaredError, VariableNotInitializedError, VariableRedeclarationError

from type import Data, Type, Variable, Array


class Visitor(baseVisitor):
    def __init__(self):
        self.data = Data()

    def visitProgram(self, ctx: kmmszarpParser.ProgramContext):
        # Get all top level variable declarations
        for stmt in ctx.statement():
            if stmt.variableDeclaration():
                variable_type = stmt.variableDeclaration().dtype().getText()
                variable_name = stmt.variableDeclaration().ID().getText()

                if variable_name in self.data.variables:
                    raise ExecutionError(ctx.start.line, ctx.start.column,
                                         f"Zmienna {variable_name} została już zadeklarowana")

                if variable_type == "liczba":
                    self.data.create_variable(variable_name, Type.INT)
                elif variable_type == "napis":
                    self.data.create_variable(variable_name, Type.STRING)
                elif variable_type == "prawdziwość":
                    self.data.create_variable(variable_name, Type.BOOL)
                else:
                    raise ExecutionError(ctx.start.line, ctx.start.column, "Nieznany typ zmiennej")

        # Execute all statements
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitFunctionCall(self, ctx: kmmszarpParser.FunctionCallContext):
        name = ctx.ID().getText()

        # TODO: Implement arguments
        args = self.visit(ctx.argumentList())

        if name == "NAPISZ":
            print(args)

    def visitIntLiteral(self, ctx: kmmszarpParser.IntLiteralContext):
        raw_value = ctx.getText()
        return Variable("_tmp", Type.INT, int(raw_value))

    def visitStringLiteral(self, ctx: kmmszarpParser.StringLiteralContext):
        raw_value = ctx.getText().replace('początek cudzysłowu ', '', 1).replace(' koniec cudzysłowu', '', 1)
        return Variable("_tmp", Type.STRING, raw_value)

    def visitBoolLiteral(self, ctx: kmmszarpParser.BoolLiteralContext):
        raw_value = ctx.getText() == "prawda"
        return Variable("_tmp", Type.BOOL, raw_value)

    #def visitPureVariableDeclaration(self, ctx: kmmszarpParser.PureVariableDeclarationContext):
    #    name = ctx.ID().getText()
    #    self.data.create_variable(name)

    def visitVariableDeclarationWithAssignment(self, ctx: kmmszarpParser.VariableDeclarationWithAssignmentContext):
        name = ctx.ID().getText()
        dtype = Type.from_string(ctx.dtype().getText())
        value = self.visit(ctx.expression())

        if dtype != value.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Nie można przypisać wartości typu {value.dtype} do zmiennej typu {dtype}")

        return self.data.set_variable(name, value)

    def visitVariableAssignment(self, ctx: kmmszarpParser.VariableAssignmentContext):
        name = ctx.ID().getText()

        if not self.data.check_if_declared(name):
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Zmienna {name} nie została zadeklarowana")

        value = self.visit(ctx.expression())
        expected_type = self.data.variables[name].dtype
        actual_type = value.dtype

        if expected_type != actual_type:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Nie można przypisać wartości typu {actual_type} do zmiennej typu {expected_type}")

        self.data.set_variable(name, value)

        return value

    def visitVariableReference(self, ctx: kmmszarpParser.VariableReferenceContext):
        name = ctx.ID().getText()
        try:
            return self.data.get_variable(name)
        except VariableNotInitializedError as e:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Zmienna {e.variable_name} nie została zainicjalizowana")
        except VariableNotDeclaredError as e:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Zmienna {e.variable_name} nie została zadeklarowana")

    def visitVariableReferencePrimary(self, ctx: kmmszarpParser.VariableReferencePrimaryContext):
        return self.visit(ctx.variableReference())

    def visitMultiplication(self, ctx: kmmszarpParser.MultiplicationContext):
        factor_1: Variable = self.visit(ctx.expression(0))
        factor_2: Variable = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if factor_1.dtype != factor_2.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można mnożyć różnych typów")

        if factor_1.dtype != Type.INT:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można mnożyć typu " + factor_1.dtype.name)

        raw_factor_1 = factor_1.value
        raw_factor_2 = factor_2.value
        result = 0

        if operator == "razy":
            result = raw_factor_1 * raw_factor_2
        elif operator == "przez":
            if raw_factor_2 == 0:
                raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można dzielić przez 0")

            result = raw_factor_1 // raw_factor_2
        else:
            result = raw_factor_1 % raw_factor_2

        return Variable("_tmp", Type.INT, result)

    def visitAddition(self, ctx: kmmszarpParser.AdditionContext):
        term_1 = self.visit(ctx.expression(0))
        term_2 = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if term_1.dtype != term_2.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można dodawać różnych typów")

        if term_1.dtype != Type.INT:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można dodawać typu " + term_1.dtype.name)

        raw_term_1 = term_1.value
        raw_term_2 = term_2.value
        result = 0

        addition = True if operator == "dodać" else False

        if addition:
            result = raw_term_1 + raw_term_2
        else:
            result = raw_term_1 - raw_term_2

        return Variable("_tmp", Type.INT, result)

    def visitComparison(self, ctx: kmmszarpParser.ComparisonContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if left.dtype != right.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można porównywać różnych typów")

        raw_left = left.value
        raw_right = right.value
        result = None

        if operator == "mniejsze niż":
            result = raw_left < raw_right
        elif operator == "większe niż":
            result = raw_left > raw_right
        elif operator == "mniejsze lub równe":
            result = raw_left <= raw_right
        elif operator == "większe lub równe":
            result = raw_left >= raw_right

        return Variable("_tmp", Type.BOOL, result)

    def visitEquality(self, ctx: kmmszarpParser.EqualityContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if left.dtype != right.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można porównywać różnych typów")

        raw_left = left.value
        raw_right = right.value
        result = None

        if operator == "równe":
            result = raw_left == raw_right
        else:
            result = raw_left != raw_right

        return Variable("_tmp", Type.BOOL, result)

    def visitParenthesizedExpression(self, ctx:kmmszarpParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expression())
