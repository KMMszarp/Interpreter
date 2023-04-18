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

        return Variable("_tmp", Type.BOOL, result)

    def visitConditionalStatement(self, ctx: kmmszarpParser.ConditionalStatementContext):
        condition_result: Variable = self.visit(ctx.expression())
        if condition_result.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column + 7, "Warunek musi być typu prawdziwość")
        if condition_result.value:
            for statement in ctx.statement():
                self.visit(statement)
            return True
        return False

    def visitConditionalStatementElse(self, ctx:kmmszarpParser.ConditionalStatementElseContext):
         if not self.visit(ctx.conditionalStatement()):
             for statement in ctx.statement():
                 self.visit(statement)

    def visitLoopWhile(self, ctx:kmmszarpParser.LoopWhileContext):
        condition_result: Variable = self.visit(ctx.expression())
        if condition_result.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column + 7, "Warunek musi być typu prawdziwość")
        while condition_result.value:
            for statement in ctx.statement():
                self.visit(statement)
            condition_result = self.visit(ctx.expression())

    def visitLoopFor(self, ctx:kmmszarpParser.LoopForContext):
        i_name = ctx.ID().getText()
        a: Variable = self.visit(ctx.expression(0))
        b: Variable = self.visit(ctx.expression(1))
        if a.dtype != Type.INT and b.dtype != Type.INT:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Końce przedziału muszą być typu liczba")
        if a.value > b.value:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Początek przedziału musi być mniejszy lub równy od końca")

        if not self.data.check_if_declared(i_name):
            raise ExecutionError(ctx.start.line, ctx.start.column, f"Zmienna {i_name} nie została zadeklarowana")

        self.data.set_variable(i_name, a)

        for i in range(a.value, b.value):
            for statement in ctx.statement():
                self.visit(statement)
            self.data.set_variable(i_name, i + 1)

    def visitParenthesizedExpression(self, ctx:kmmszarpParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expression())

    def visitNegation(self, ctx:kmmszarpParser.NegationContext):
        expression: Variable = self.visit(ctx.expression())
        if expression.dtype != Type.BOOL:
            raise ExecutionError(ctx.start.line, ctx.start.column, "Negacja musi być typu prawdziwość")
        return Variable("_tmp", Type.BOOL, not expression.value)

    def visitCast(self, ctx:kmmszarpParser.CastContext):
        expression: Variable = self.visit(ctx.expression())
        type = ctx.dtype().getText()
        name = expression.name
        value = expression.value

        if type == "liczba":
            if expression.dtype == Type.INT:
                return expression
            elif expression.dtype == Type.BOOL:
                self.data.remove_variable(name)
                self.data.create_and_initialize_variable(name, Type.INT, 1 if value else 0)
                return Variable("_tmp", Type.INT, 1 if value else 0)
            else:
                try:
                    self.data.remove_variable(name)
                    self.data.create_and_initialize_variable(name, Type.INT, int(value))
                    return Variable("_tmp", Type.INT, int(value))
                except ValueError:
                    raise ExecutionError(ctx.start.line, ctx.start.column, "Nie można rzutować typu napis na typ liczba")

        elif type == "napis":
            if expression.dtype == Type.STRING:
                return expression
            elif expression.dtype == Type.INT:
                self.data.remove_variable(name)
                self.data.create_and_initialize_variable(name, Type.STRING, str(value))
                return Variable("_tmp", Type.STRING, str(expression.value))
            else:
                self.data.remove_variable(name)
                self.data.create_and_initialize_variable(name, Type.STRING, "prawda" if value else "fałsz")
                return Variable("_tmp", Type.STRING, "prawda" if expression.value else "fałsz")

        else:
            if expression.dtype == Type.INT:
                self.data.remove_variable(name)
                self.data.create_and_initialize_variable(name, Type.BOOL, True if value else False)
                return Variable("_tmp", Type.BOOL, True if expression.value else False)
            elif expression.dtype == Type.STRING:
                self.data.remove_variable(name)
                self.data.create_and_initialize_variable(name, Type.BOOL, True if value else False)
                return Variable("_tmp", Type.BOOL, True if expression.value else False)
            else:
                return expression



