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


    # Enter a parse tree produced by kmmszarpParser#conditional.
    def enterConditional(self, ctx:kmmszarpParser.ConditionalContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#conditional.
    def exitConditional(self, ctx:kmmszarpParser.ConditionalContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#ifelse.
    def enterIfelse(self, ctx:kmmszarpParser.IfelseContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#ifelse.
    def exitIfelse(self, ctx:kmmszarpParser.IfelseContext):
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


    # Enter a parse tree produced by kmmszarpParser#expression.
    def enterExpression(self, ctx:kmmszarpParser.ExpressionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#expression.
    def exitExpression(self, ctx:kmmszarpParser.ExpressionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#logicOr.
    def enterLogicOr(self, ctx:kmmszarpParser.LogicOrContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#logicOr.
    def exitLogicOr(self, ctx:kmmszarpParser.LogicOrContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#logicAnd.
    def enterLogicAnd(self, ctx:kmmszarpParser.LogicAndContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#logicAnd.
    def exitLogicAnd(self, ctx:kmmszarpParser.LogicAndContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#equality.
    def enterEquality(self, ctx:kmmszarpParser.EqualityContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#equality.
    def exitEquality(self, ctx:kmmszarpParser.EqualityContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#comparison.
    def enterComparison(self, ctx:kmmszarpParser.ComparisonContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#comparison.
    def exitComparison(self, ctx:kmmszarpParser.ComparisonContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#addition.
    def enterAddition(self, ctx:kmmszarpParser.AdditionContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#addition.
    def exitAddition(self, ctx:kmmszarpParser.AdditionContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#multiplication.
    def enterMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#multiplication.
    def exitMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#primary.
    def enterPrimary(self, ctx:kmmszarpParser.PrimaryContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#primary.
    def exitPrimary(self, ctx:kmmszarpParser.PrimaryContext):
        pass


    # Enter a parse tree produced by kmmszarpParser#type.
    def enterType(self, ctx:kmmszarpParser.TypeContext):
        pass

    # Exit a parse tree produced by kmmszarpParser#type.
    def exitType(self, ctx:kmmszarpParser.TypeContext):
        pass



del kmmszarpParser