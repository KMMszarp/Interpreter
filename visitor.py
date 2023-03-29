import antlr4

from kmmszarp.kmmszarpVisitor import kmmszarpVisitor as baseVisitor
from kmmszarp.kmmszarpParser import kmmszarpParser


# TODO: Remove this function and replace it with a proper visitor
def handle_print(ctx: kmmszarpParser.ExpressionContext):
    # Very dirty parsing of the print expression starts here

    # Need to go all the way down to the string
    # To be on the safe side assert that the structure is as expected
    expression_context = ctx.getChild(0)
    assert isinstance(expression_context, kmmszarpParser.ExpressionContext)
    logic_or_context = expression_context.getChild(0)
    assert isinstance(logic_or_context, kmmszarpParser.LogicOrContext)
    logic_and_context = logic_or_context.getChild(0)
    assert isinstance(logic_and_context, kmmszarpParser.LogicAndContext)
    equality_context = logic_and_context.getChild(0)
    assert isinstance(equality_context, kmmszarpParser.EqualityContext)
    comparison_context = equality_context.getChild(0)
    assert isinstance(comparison_context, kmmszarpParser.ComparisonContext)
    addition_context = comparison_context.getChild(0)
    assert isinstance(addition_context, kmmszarpParser.AdditionContext)
    multiplication_context = addition_context.getChild(0)
    assert isinstance(multiplication_context, kmmszarpParser.MultiplicationContext)
    primary_context = multiplication_context.getChild(0)
    assert isinstance(primary_context, kmmszarpParser.PrimaryContext)

    # Check if the primary type is a string indeed
    full_string = primary_context.STRING()
    assert full_string is not None

    # Remove the quotes from the string
    full_string_text = full_string.getText()
    string = full_string_text[20:-18]

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
