# Generated from ./kmmszarp.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kmmszarpParser import kmmszarpParser
else:
    from kmmszarpParser import kmmszarpParser

# This class defines a complete generic visitor for a parse tree produced by kmmszarpParser.

class kmmszarpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by kmmszarpParser#program.
    def visitProgram(self, ctx:kmmszarpParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#statement.
    def visitStatement(self, ctx:kmmszarpParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#loopFor.
    def visitLoopFor(self, ctx:kmmszarpParser.LoopForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#loopWhile.
    def visitLoopWhile(self, ctx:kmmszarpParser.LoopWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#conditional.
    def visitConditional(self, ctx:kmmszarpParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#ifelse.
    def visitIfelse(self, ctx:kmmszarpParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:kmmszarpParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#parameterList.
    def visitParameterList(self, ctx:kmmszarpParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#parameter.
    def visitParameter(self, ctx:kmmszarpParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#returnStatement.
    def visitReturnStatement(self, ctx:kmmszarpParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:kmmszarpParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:kmmszarpParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#arrayValue.
    def visitArrayValue(self, ctx:kmmszarpParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#variableReference.
    def visitVariableReference(self, ctx:kmmszarpParser.VariableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#arrayAccess.
    def visitArrayAccess(self, ctx:kmmszarpParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#variableAssignment.
    def visitVariableAssignment(self, ctx:kmmszarpParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#arrayAssignment.
    def visitArrayAssignment(self, ctx:kmmszarpParser.ArrayAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#functionCall.
    def visitFunctionCall(self, ctx:kmmszarpParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#argumentList.
    def visitArgumentList(self, ctx:kmmszarpParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#expression.
    def visitExpression(self, ctx:kmmszarpParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#logicOr.
    def visitLogicOr(self, ctx:kmmszarpParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#logicAnd.
    def visitLogicAnd(self, ctx:kmmszarpParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#equality.
    def visitEquality(self, ctx:kmmszarpParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#comparison.
    def visitComparison(self, ctx:kmmszarpParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#addition.
    def visitAddition(self, ctx:kmmszarpParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#multiplication.
    def visitMultiplication(self, ctx:kmmszarpParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#primary.
    def visitPrimary(self, ctx:kmmszarpParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kmmszarpParser#type.
    def visitType(self, ctx:kmmszarpParser.TypeContext):
        return self.visitChildren(ctx)



del kmmszarpParser