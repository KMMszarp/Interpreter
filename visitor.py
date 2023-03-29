import antlr4

from kmmszarp.kmmszarpVisitor import kmmszarpVisitor as baseVisitor
from kmmszarp.kmmszarpParser import kmmszarpParser


# TODO: Remove this function and replace it with a proper visitor
def handle_print(ctx: kmmszarpParser.ExpressionContext):
    # Very dirty parsing of the print expression starts here
    full_string = ctx.getText()
    string = full_string[20:-18]

    # Very dirty parsing of the print expression ends here
    print(string)


class Visitor(baseVisitor):
    def visitFunctionCall(self, ctx: kmmszarpParser.FunctionCallContext):
        children = [*ctx.getChildren()]

        if not isinstance(children[1], antlr4.tree.Tree.TerminalNodeImpl):
            raise SyntaxError("Expected a function name, got " + str(type(children[1])) + " instead")

        function_name = children[1].getText()
        if function_name == "NAPISZ":
            handle_print(children[2])
            return None

        return super().visitFunctionCall(ctx)

    def visitIntLiteral(self, ctx: kmmszarpParser.IntLiteralContext):
        return int(ctx.getText())

    def visitStringLiteral(self, ctx: kmmszarpParser.StringLiteralContext):
        return ctx.getText()

    def visitBoolLiteral(self, ctx: kmmszarpParser.BoolLiteralContext):
        return ctx.getText() == "prawda"

    def visitPureVariableDeclaration(self, ctx: kmmszarpParser.PureVariableDeclarationContext):
        name = ctx.ID().getText()

        print(name)

    def visitVariableDeclarationWithAssignment(self, ctx: kmmszarpParser.VariableDeclarationWithAssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())

        print(name, value)
        return value

    def visitVariableAssignment(self, ctx: kmmszarpParser.VariableAssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())

        print(name, value)
        return value

    def visitMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        factor_1 = self.visit(ctx.expression(0))
        factor_2 = self.visit(ctx.expression(1))
        operator = ctx.op.text

        multiplication = True if operator == "razy" else False

        if multiplication:
            return factor_1 * factor_2

        return factor_1 // factor_2

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
