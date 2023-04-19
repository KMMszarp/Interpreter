from kmmszarp.kmmszarpVisitor import kmmszarpVisitor as baseVisitor
from kmmszarp.kmmszarpParser import kmmszarpParser
from err import ExecutionError, VariableNotDeclaredError, VariableNotInitializedError, VariableRedeclarationError

from type import Data, Type, Variable, ParsedExpression, VariableLike


class Visitor(baseVisitor):
    def __init__(self):
        self.data = Data()

    def visitProgram(self, ctx: kmmszarpParser.ProgramContext):
        # Get all top level variable declarations
        for stmt in ctx.statement():
            if stmt.variableDeclaration():
                vd = stmt.variableDeclaration()
                variable_type = None
                variable_name = None

                if vd.pureVariableDeclaration():
                    variable_type = vd.pureVariableDeclaration().dtype().getText()
                    variable_name = vd.pureVariableDeclaration().ID().getText()
                elif vd.variableDeclarationWithAssignment():
                    variable_type = vd.variableDeclarationWithAssignment().dtype().getText()
                    variable_name = vd.variableDeclarationWithAssignment().ID().getText()

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
        return ParsedExpression(Type.INT, int(raw_value))

    def visitUnaryMinus(self, ctx:kmmszarpParser.UnaryMinusContext):
        expr = self.visit(ctx.expression())
        if expr.dtype != Type.INT:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można odjąć od wartości typu napis")
        return ParsedExpression(Type.INT, -expr.value)

    def visitStringLiteral(self, ctx: kmmszarpParser.StringLiteralContext):
        raw_value = ctx.getText().replace('początek cudzysłowu ', '', 1).replace(' koniec cudzysłowu', '', 1)
        return ParsedExpression(Type.STRING, raw_value)

    def visitBoolLiteral(self, ctx: kmmszarpParser.BoolLiteralContext):
        raw_value = ctx.getText() == "prawda"
        return ParsedExpression(Type.BOOL, raw_value)

    #def visitPureVariableDeclaration(self, ctx: kmmszarpParser.PureVariableDeclarationContext):
    #    name = ctx.ID().getText()
    #    self.data.create_variable(name)

    def visitVariableDeclarationWithAssignment(self, ctx: kmmszarpParser.VariableDeclarationWithAssignmentContext):
        name = ctx.ID().getText()
        dtype = Type.from_string(ctx.dtype().getText())
        value: VariableLike = self.visit(ctx.expression())

        if dtype != value.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Nie można przypisać wartości typu {value.dtype} do zmiennej typu {dtype}")

        return self.data.set_variable(name, value)

    def visitVariableAssignment(self, ctx: kmmszarpParser.VariableAssignmentContext):
        name = ctx.ID().getText()

        if not self.data.check_if_declared(name):
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Zmienna {name} nie została zadeklarowana")

        value: VariableLike = self.visit(ctx.expression())
        expected_type = self.data.variables[name].dtype
        actual_type = value.dtype

        if expected_type != actual_type:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 f"Nie można przypisać wartości typu {actual_type} do zmiennej typu {expected_type}")

        return self.data.set_variable(name, value)

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
        factor_1: VariableLike = self.visit(ctx.expression(0))
        factor_2: VariableLike = self.visit(ctx.expression(1))
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

        return ParsedExpression(Type.INT, result)

    def visitAddition(self, ctx: kmmszarpParser.AdditionContext):
        term_1: VariableLike = self.visit(ctx.expression(0))
        term_2: VariableLike = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if term_1.dtype != term_2.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można dodawać różnych typów")

        if term_1.dtype == Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można dodawać typu " + term_1.dtype.name)

        raw_term_1 = term_1.value
        raw_term_2 = term_2.value

        addition = True if operator == "dodać" else False

        if term_1.dtype == Type.INT:
            result = 0
            if addition:
                result = raw_term_1 + raw_term_2
            else:
                result = raw_term_1 - raw_term_2

            return ParsedExpression(Type.INT, result)

        if addition:
            result = raw_term_1 + raw_term_2
            return ParsedExpression(Type.STRING, result)
        else:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można odejmować typu STRING")

    def visitComparison(self, ctx: kmmszarpParser.ComparisonContext):
        left: VariableLike = self.visit(ctx.expression(0))
        right: VariableLike = self.visit(ctx.expression(1))
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

        return ParsedExpression(Type.BOOL, result)

    def visitEquality(self, ctx: kmmszarpParser.EqualityContext):
        left: VariableLike = self.visit(ctx.expression(0))
        right: VariableLike = self.visit(ctx.expression(1))
        operator = ctx.eq.text

        if left.dtype != right.dtype:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można porównywać różnych typów")

        raw_left = left.value
        raw_right = right.value
        result = None

        if operator == "równe":
            result = raw_left == raw_right
        else:
            result = raw_left != raw_right

        return ParsedExpression(Type.BOOL, result)
    
    def visitLogicAnd(self, ctx: kmmszarpParser.LogicAndContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if left.dtype != Type.BOOL or right.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Operacja logiczna AND wymaga typu prawdziwość")

        result = left.value and right.value

        return ParsedExpression(Type.BOOL, result)

    def visitLogicOr(self, ctx: kmmszarpParser.LogicOrContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if left.dtype != Type.BOOL or right.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Operacja logiczna OR wymaga typu prawdziwość")

        result = left.value or right.value

        return ParsedExpression(Type.BOOL, result)

    def visitConditionalStatement(self, ctx: kmmszarpParser.ConditionalStatementContext) -> bool:
        condition_result: VariableLike = self.visit(ctx.expression())

        if condition_result.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column + 7, "Warunek musi być typu prawdziwość")
        if condition_result.value:
            for statement in ctx.statement():
                self.visit(statement)
            return True
        return False

    def visitConditionalStatementElse(self, ctx: kmmszarpParser.ConditionalStatementElseContext):
        if not self.visit(ctx.conditionalStatement()):
            for statement in ctx.statement():
                self.visit(statement)

    def visitLoopWhile(self, ctx: kmmszarpParser.LoopWhileContext):
        condition_result: VariableLike = self.visit(ctx.expression())

        if condition_result.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column + 7, "Warunek musi być typu prawdziwość")

        while condition_result.value:
            for statement in ctx.statement():
                self.visit(statement)
            condition_result = self.visit(ctx.expression())

    def visitLoopFor(self, ctx:kmmszarpParser.LoopForContext):
        i_name = ctx.ID().getText()
        a: VariableLike = self.visit(ctx.expression(0))
        b: VariableLike = self.visit(ctx.expression(1))

        if a.dtype != Type.INT and b.dtype != Type.INT:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Końce przedziału muszą być typu liczba")
        if a.value > b.value:
            raise ExecutionError(ctx.start.line, ctx.start.column,
                                 "Początek przedziału musi być mniejszy lub równy od końca")

        if not self.data.check_if_declared(i_name):
            raise ExecutionError(ctx.start.line, ctx.start.column, f"Zmienna {i_name} nie została zadeklarowana")

        self.data.set_variable(i_name, a)

        for i in range(a.value, b.value):
            for statement in ctx.statement():
                self.visit(statement)
            self.data.set_variable(i_name, i + 1)

    def visitParenthesizedExpression(self, ctx: kmmszarpParser.ParenthesizedExpressionContext) -> VariableLike:
        return self.visit(ctx.expression())

    def visitNegation(self, ctx: kmmszarpParser.NegationContext):
        expression: VariableLike = self.visit(ctx.expression())

        if expression.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Negacja musi być typu prawdziwość")

        return VariableLike(Type.BOOL, not expression.value)

    def visitCastExpression(self, ctx: kmmszarpParser.CastExpressionContext) -> ParsedExpression:
        return self.visit(ctx.cast())

    def visitCast(self, ctx: kmmszarpParser.CastContext):
        expression: VariableLike = self.visit(ctx.expression())
        dtype = ctx.dtype().getText()
        value = expression.value

        if dtype == "liczba":
            if expression.dtype == Type.INT:
                return expression
            elif expression.dtype == Type.BOOL:
                return ParsedExpression(Type.INT, 1 if value else 0)
            else:
                try:
                    return ParsedExpression(Type.INT, int(value))
                except ValueError:
                    raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można rzutować typu napis na typ liczba")

        elif dtype == "napis":
            if expression.dtype == Type.STRING:
                return expression
            elif expression.dtype == Type.INT:
                if expression.value < 0:
                    val = "minus " + str(abs(expression.value))
                else:
                    val = str(abs(expression.value))
                return ParsedExpression(Type.STRING, val)
            else:
                return ParsedExpression(Type.STRING, "prawda" if expression.value else "fałsz")

        else:
            if expression.dtype == Type.INT:
                return ParsedExpression(Type.BOOL, True if expression.value else False)
            elif expression.dtype == Type.STRING:
                return ParsedExpression(Type.BOOL, True if expression.value != "0" else False)
            else:
                return expression
