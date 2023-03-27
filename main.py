import sys

import antlr4

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser


def handle_print(print_expr):
    # Very dirty parsing of the print expression starts here

    # Need to go all the way down to the string
    # To be on the safe side assert that the structure is as expected
    expression_context = print_expr.getChild(0)
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


def handle_function_call(call):
    children = [*call.getChildren()]

    # Chyba niepotrzebne
    # assert children[0].getText() == "wywołaj"
    # assert isinstance(children[1], antlr4.tree.Tree.TerminalNodeImpl)

    if not isinstance(children[1], antlr4.tree.Tree.TerminalNodeImpl):
        raise SyntaxError("Expected a function name, got " + str(type(children[1])) + " instead")

    function_name = children[1].getText()
    if function_name == "napisz":
        handle_print(children[2])
    else:
        raise NotImplementedError("Not able to handle function " + function_name)


def handle_statement(stmt):
    for child in stmt.getChildren():
        if isinstance(child, kmmszarpParser.FunctionCallContext):
            handle_function_call(child)
        else:
            raise NotImplementedError("Not able to handle " + str(type(child)) + " yet")


def handle_expression(expr):
    for child in expr.getChildren():
        if isinstance(child, kmmszarpParser.StatementContext):
            handle_statement(child)
        elif isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
            pass
        else:
            raise NotImplementedError("Not able to handle " + str(type(child)) + " yet")


def main(argv):
    input_stream = antlr4.FileStream(argv[1], encoding="utf-8")
    lexer = kmmszarpLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = kmmszarpParser(stream)
    tree = parser.program()
    handle_expression(tree)


if __name__ == '__main__':
    main(sys.argv)
