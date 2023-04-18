# Generated from ./kmmszarp.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kmmszarpParser import kmmszarpParser
else:
    from kmmszarpParser import kmmszarpParser

# This class defines a complete listener for a parse tree produced by kmmszarpParser.
class kmmszarpListener(ParseTreeListener):

    # Enter a parse tree produced by kmmszarpParser#program.
    def enterProgram(self, ctx:kmmszarpParser.ProgramContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#program.
    def exitProgram(self, ctx:kmmszarpParser.ProgramContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#statement.
    def enterStatement(self, ctx:kmmszarpParser.StatementContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#statement.
    def exitStatement(self, ctx:kmmszarpParser.StatementContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#loopFor.
    def enterLoopFor(self, ctx:kmmszarpParser.LoopForContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#loopFor.
    def exitLoopFor(self, ctx:kmmszarpParser.LoopForContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#loopWhile.
    def enterLoopWhile(self, ctx:kmmszarpParser.LoopWhileContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#loopWhile.
    def exitLoopWhile(self, ctx:kmmszarpParser.LoopWhileContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:kmmszarpParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:kmmszarpParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#conditionalStatementElse.
    def enterConditionalStatementElse(self, ctx:kmmszarpParser.ConditionalStatementElseContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#conditionalStatementElse.
    def exitConditionalStatementElse(self, ctx:kmmszarpParser.ConditionalStatementElseContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:kmmszarpParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:kmmszarpParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#parameterList.
    def enterParameterList(self, ctx:kmmszarpParser.ParameterListContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#parameterList.
    def exitParameterList(self, ctx:kmmszarpParser.ParameterListContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#parameter.
    def enterParameter(self, ctx:kmmszarpParser.ParameterContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#parameter.
    def exitParameter(self, ctx:kmmszarpParser.ParameterContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#returnStatement.
    def enterReturnStatement(self, ctx:kmmszarpParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#returnStatement.
    def exitReturnStatement(self, ctx:kmmszarpParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#pureVariableDeclaration.
    def enterPureVariableDeclaration(self, ctx:kmmszarpParser.PureVariableDeclarationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#pureVariableDeclaration.
    def exitPureVariableDeclaration(self, ctx:kmmszarpParser.PureVariableDeclarationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#variableDeclarationWithAssignment.
    def enterVariableDeclarationWithAssignment(self, ctx:kmmszarpParser.VariableDeclarationWithAssignmentContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#variableDeclarationWithAssignment.
    def exitVariableDeclarationWithAssignment(self, ctx:kmmszarpParser.VariableDeclarationWithAssignmentContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:kmmszarpParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:kmmszarpParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:kmmszarpParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:kmmszarpParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#arrayValue.
    def enterArrayValue(self, ctx:kmmszarpParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#arrayValue.
    def exitArrayValue(self, ctx:kmmszarpParser.ArrayValueContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#variableReference.
    def enterVariableReference(self, ctx:kmmszarpParser.VariableReferenceContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#variableReference.
    def exitVariableReference(self, ctx:kmmszarpParser.VariableReferenceContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#arrayAccess.
    def enterArrayAccess(self, ctx:kmmszarpParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#arrayAccess.
    def exitArrayAccess(self, ctx:kmmszarpParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#variableAssignment.
    def enterVariableAssignment(self, ctx:kmmszarpParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#variableAssignment.
    def exitVariableAssignment(self, ctx:kmmszarpParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#arrayAssignment.
    def enterArrayAssignment(self, ctx:kmmszarpParser.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#arrayAssignment.
    def exitArrayAssignment(self, ctx:kmmszarpParser.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#functionCall.
    def enterFunctionCall(self, ctx:kmmszarpParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#functionCall.
    def exitFunctionCall(self, ctx:kmmszarpParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#argumentList.
    def enterArgumentList(self, ctx:kmmszarpParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#argumentList.
    def exitArgumentList(self, ctx:kmmszarpParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#cast.
    def enterCast(self, ctx:kmmszarpParser.CastContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#cast.
    def exitCast(self, ctx:kmmszarpParser.CastContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:kmmszarpParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:kmmszarpParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#LogicOr.
    def enterLogicOr(self, ctx:kmmszarpParser.LogicOrContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#LogicOr.
    def exitLogicOr(self, ctx:kmmszarpParser.LogicOrContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#Multiplication.
    def enterMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#Multiplication.
    def exitMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#Addition.
    def enterAddition(self, ctx:kmmszarpParser.AdditionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#Addition.
    def exitAddition(self, ctx:kmmszarpParser.AdditionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#Negation.
    def enterNegation(self, ctx:kmmszarpParser.NegationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#Negation.
    def exitNegation(self, ctx:kmmszarpParser.NegationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#PrimaryExpression.
    def enterPrimaryExpression(self, ctx:kmmszarpParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#PrimaryExpression.
    def exitPrimaryExpression(self, ctx:kmmszarpParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#Comparison.
    def enterComparison(self, ctx:kmmszarpParser.ComparisonContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#Comparison.
    def exitComparison(self, ctx:kmmszarpParser.ComparisonContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#Equality.
    def enterEquality(self, ctx:kmmszarpParser.EqualityContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#Equality.
    def exitEquality(self, ctx:kmmszarpParser.EqualityContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#LogicAnd.
    def enterLogicAnd(self, ctx:kmmszarpParser.LogicAndContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#LogicAnd.
    def exitLogicAnd(self, ctx:kmmszarpParser.LogicAndContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#IntLiteral.
    def enterIntLiteral(self, ctx:kmmszarpParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#IntLiteral.
    def exitIntLiteral(self, ctx:kmmszarpParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#StringLiteral.
    def enterStringLiteral(self, ctx:kmmszarpParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#StringLiteral.
    def exitStringLiteral(self, ctx:kmmszarpParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#BoolLiteral.
    def enterBoolLiteral(self, ctx:kmmszarpParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#BoolLiteral.
    def exitBoolLiteral(self, ctx:kmmszarpParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#VariableReferencePrimary.
    def enterVariableReferencePrimary(self, ctx:kmmszarpParser.VariableReferencePrimaryContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#VariableReferencePrimary.
    def exitVariableReferencePrimary(self, ctx:kmmszarpParser.VariableReferencePrimaryContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#dtype.
    def enterDtype(self, ctx:kmmszarpParser.DtypeContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#dtype.
    def exitDtype(self, ctx:kmmszarpParser.DtypeContext):
        pass



del kmmszarpParser