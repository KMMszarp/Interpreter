from kmmszarp.kmmszarpVisitor import kmmszarpVisitor as baseVisitor
from kmmszarp.kmmszarpParser import kmmszarpParser

from type import Data


class Visitor(baseVisitor):
    def __init__(self):
        self.data = Data()

    def visitFunctionCall(self, ctx: kmmszarpParser.FunctionCallContext):
        name = ctx.ID().getText()

        # TODO: Implement arguments
        args = self.visit(ctx.argumentList())

        if name == "NAPISZ":
            print(args)

    def visitIntLiteral(self, ctx: kmmszarpParser.IntLiteralContext):
        return int(ctx.getText())

    def visitStringLiteral(self, ctx: kmmszarpParser.StringLiteralContext):
        return ctx.getText().replace('początek cudzysłowu ', '', 1).replace(' koniec cudzysłowu', '', 1)

    def visitBoolLiteral(self, ctx: kmmszarpParser.BoolLiteralContext):
        return ctx.getText() == "prawda"

    def visitPureVariableDeclaration(self, ctx: kmmszarpParser.PureVariableDeclarationContext):
        name = ctx.ID().getText()
        self.data.create_variable(name)

    def visitVariableDeclarationWithAssignment(self, ctx: kmmszarpParser.VariableDeclarationWithAssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())

        self.data.create_and_initialize_variable(name, value)
        return value

    def visitVariableAssignment(self, ctx: kmmszarpParser.VariableAssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())

        self.data.initialize_variable(name, value)
        return value

    def visitVariableReference(self, ctx: kmmszarpParser.VariableReferenceContext):
        name = ctx.ID().getText()
        return self.data.get_variable(name)

    def visitVariableReferencePrimary(self, ctx: kmmszarpParser.VariableReferencePrimaryContext):
        return self.visit(ctx.variableReference())

    def visitMultiplication(self, ctx: kmmszarpParser.MultiplicationContext):
        factor_1 = self.visit(ctx.expression(0))
        factor_2 = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if operator == "razy":
            return factor_1 * factor_2

        if operator == "przez":
            return factor_1 // factor_2

        return factor_1 % factor_2

    def visitAddition(self, ctx: kmmszarpParser.AdditionContext):
        term_1 = self.visit(ctx.expression(0))
        term_2 = self.visit(ctx.expression(1))
        operator = ctx.op.text

        addition = True if operator == "dodać" else False

        if addition:
            return term_1 + term_2

        return term_1 - term_2

    def visitComparison(self, ctx: kmmszarpParser.ComparisonContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if operator == "mniejsze niż":
            return left < right
        elif operator == "większe niż":
            return left > right
        elif operator == "mniejsze lub równe":
            return left <= right
        elif operator == "większe lub równe":
            return left >= right

    def visitEquality(self, ctx: kmmszarpParser.EqualityContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if operator == "równe":
            return left == right

        return left != right
