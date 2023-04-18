# Generated from ./kmmszarp.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,3,0,49,8,0,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,79,8,2,10,2,12,2,82,9,
        2,1,2,1,2,1,2,5,2,87,8,2,10,2,12,2,90,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,5,3,99,8,3,10,3,12,3,102,9,3,1,3,1,3,1,3,5,3,107,8,3,10,3,
        12,3,110,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,119,8,4,10,4,12,4,122,
        9,4,1,4,1,4,1,4,5,4,127,8,4,10,4,12,4,130,9,4,1,4,1,4,1,5,1,5,5,
        5,136,8,5,10,5,12,5,139,9,5,1,5,1,5,1,5,5,5,144,8,5,10,5,12,5,147,
        9,5,1,5,1,5,1,5,5,5,152,8,5,10,5,12,5,155,9,5,1,5,1,5,1,6,1,6,1,
        6,1,6,3,6,163,8,6,1,6,1,6,1,6,1,6,5,6,169,8,6,10,6,12,6,172,9,6,
        1,6,1,6,1,6,5,6,177,8,6,10,6,12,6,180,9,6,1,6,3,6,183,8,6,1,6,5,
        6,186,8,6,10,6,12,6,189,9,6,1,6,1,6,1,7,1,7,1,7,5,7,196,8,7,10,7,
        12,7,199,9,7,3,7,201,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,220,8,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,5,11,229,8,11,10,11,12,11,232,9,11,1,11,1,
        11,3,11,236,8,11,1,12,1,12,1,13,1,13,3,13,242,8,13,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,18,1,18,3,18,266,8,18,1,18,1,18,1,18,3,18,
        271,8,18,5,18,273,8,18,10,18,12,18,276,9,18,3,18,278,8,18,1,19,1,
        19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,306,
        8,20,10,20,12,20,309,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,319,8,21,1,22,1,22,1,22,1,187,1,40,23,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,5,1,0,31,33,1,0,34,35,
        1,0,36,39,1,0,40,41,1,0,44,47,346,0,53,1,0,0,0,2,67,1,0,0,0,4,69,
        1,0,0,0,6,93,1,0,0,0,8,113,1,0,0,0,10,133,1,0,0,0,12,158,1,0,0,0,
        14,200,1,0,0,0,16,202,1,0,0,0,18,206,1,0,0,0,20,219,1,0,0,0,22,221,
        1,0,0,0,24,237,1,0,0,0,26,241,1,0,0,0,28,243,1,0,0,0,30,248,1,0,
        0,0,32,252,1,0,0,0,34,259,1,0,0,0,36,277,1,0,0,0,38,279,1,0,0,0,
        40,284,1,0,0,0,42,318,1,0,0,0,44,320,1,0,0,0,46,48,3,2,1,0,47,49,
        5,57,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,52,1,0,0,0,50,52,5,57,0,
        0,51,46,1,0,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,1,1,0,0,0,55,53,1,0,0,0,56,68,3,4,2,0,57,68,3,6,3,0,58,
        68,3,8,4,0,59,68,3,10,5,0,60,68,3,12,6,0,61,68,3,20,10,0,62,68,3,
        22,11,0,63,68,3,30,15,0,64,68,3,32,16,0,65,68,3,34,17,0,66,68,3,
        38,19,0,67,56,1,0,0,0,67,57,1,0,0,0,67,58,1,0,0,0,67,59,1,0,0,0,
        67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,1,
        0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,5,1,0,0,70,
        71,5,2,0,0,71,72,3,20,10,0,72,73,5,3,0,0,73,74,3,40,20,0,74,75,5,
        4,0,0,75,76,3,40,20,0,76,80,5,5,0,0,77,79,5,57,0,0,78,77,1,0,0,0,
        79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,88,1,0,0,0,82,80,1,
        0,0,0,83,84,3,2,1,0,84,85,5,57,0,0,85,87,1,0,0,0,86,83,1,0,0,0,87,
        90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,
        0,91,92,5,6,0,0,92,5,1,0,0,0,93,94,5,1,0,0,94,95,5,7,0,0,95,96,3,
        40,20,0,96,100,5,5,0,0,97,99,5,57,0,0,98,97,1,0,0,0,99,102,1,0,0,
        0,100,98,1,0,0,0,100,101,1,0,0,0,101,108,1,0,0,0,102,100,1,0,0,0,
        103,104,3,2,1,0,104,105,5,57,0,0,105,107,1,0,0,0,106,103,1,0,0,0,
        107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,
        110,108,1,0,0,0,111,112,5,6,0,0,112,7,1,0,0,0,113,114,5,8,0,0,114,
        115,3,40,20,0,115,116,5,9,0,0,116,120,5,10,0,0,117,119,5,57,0,0,
        118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,
        121,128,1,0,0,0,122,120,1,0,0,0,123,124,3,2,1,0,124,125,5,57,0,0,
        125,127,1,0,0,0,126,123,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,
        128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,11,0,0,
        132,9,1,0,0,0,133,137,3,8,4,0,134,136,5,57,0,0,135,134,1,0,0,0,136,
        139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,
        137,1,0,0,0,140,141,5,12,0,0,141,145,5,10,0,0,142,144,5,57,0,0,143,
        142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,
        153,1,0,0,0,147,145,1,0,0,0,148,149,3,2,1,0,149,150,5,57,0,0,150,
        152,1,0,0,0,151,148,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,
        154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,5,11,0,0,157,
        11,1,0,0,0,158,159,5,13,0,0,159,162,5,49,0,0,160,161,5,14,0,0,161,
        163,3,14,7,0,162,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,
        165,5,15,0,0,165,166,3,44,22,0,166,170,5,16,0,0,167,169,5,57,0,0,
        168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,
        171,178,1,0,0,0,172,170,1,0,0,0,173,174,3,2,1,0,174,175,5,57,0,0,
        175,177,1,0,0,0,176,173,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,
        178,179,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,181,183,3,18,9,0,
        182,181,1,0,0,0,182,183,1,0,0,0,183,187,1,0,0,0,184,186,5,57,0,0,
        185,184,1,0,0,0,186,189,1,0,0,0,187,188,1,0,0,0,187,185,1,0,0,0,
        188,190,1,0,0,0,189,187,1,0,0,0,190,191,5,17,0,0,191,13,1,0,0,0,
        192,197,3,16,8,0,193,194,5,18,0,0,194,196,3,16,8,0,195,193,1,0,0,
        0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,201,1,0,0,
        0,199,197,1,0,0,0,200,192,1,0,0,0,200,201,1,0,0,0,201,15,1,0,0,0,
        202,203,5,19,0,0,203,204,3,44,22,0,204,205,5,49,0,0,205,17,1,0,0,
        0,206,207,5,20,0,0,207,208,3,40,20,0,208,19,1,0,0,0,209,210,5,19,
        0,0,210,211,3,44,22,0,211,212,5,49,0,0,212,220,1,0,0,0,213,214,5,
        19,0,0,214,215,3,44,22,0,215,216,5,49,0,0,216,217,5,21,0,0,217,218,
        3,40,20,0,218,220,1,0,0,0,219,209,1,0,0,0,219,213,1,0,0,0,220,21,
        1,0,0,0,221,222,5,22,0,0,222,223,3,44,22,0,223,224,5,49,0,0,224,
        225,5,21,0,0,225,230,3,24,12,0,226,227,5,18,0,0,227,229,3,24,12,
        0,228,226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,
        0,231,235,1,0,0,0,232,230,1,0,0,0,233,234,5,23,0,0,234,236,5,51,
        0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,23,1,0,0,0,237,238,3,40,
        20,0,238,25,1,0,0,0,239,242,5,49,0,0,240,242,3,28,14,0,241,239,1,
        0,0,0,241,240,1,0,0,0,242,27,1,0,0,0,243,244,5,24,0,0,244,245,3,
        40,20,0,245,246,5,25,0,0,246,247,3,40,20,0,247,29,1,0,0,0,248,249,
        5,49,0,0,249,250,5,21,0,0,250,251,3,40,20,0,251,31,1,0,0,0,252,253,
        5,26,0,0,253,254,3,40,20,0,254,255,5,27,0,0,255,256,3,40,20,0,256,
        257,5,28,0,0,257,258,3,40,20,0,258,33,1,0,0,0,259,260,5,29,0,0,260,
        261,5,49,0,0,261,262,3,36,18,0,262,35,1,0,0,0,263,266,3,20,10,0,
        264,266,3,40,20,0,265,263,1,0,0,0,265,264,1,0,0,0,266,274,1,0,0,
        0,267,270,5,18,0,0,268,271,3,20,10,0,269,271,3,40,20,0,270,268,1,
        0,0,0,270,269,1,0,0,0,271,273,1,0,0,0,272,267,1,0,0,0,273,276,1,
        0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,278,1,0,0,0,276,274,1,
        0,0,0,277,265,1,0,0,0,277,278,1,0,0,0,278,37,1,0,0,0,279,280,5,30,
        0,0,280,281,3,40,20,0,281,282,5,27,0,0,282,283,3,44,22,0,283,39,
        1,0,0,0,284,285,6,20,-1,0,285,286,3,42,21,0,286,307,1,0,0,0,287,
        288,10,7,0,0,288,289,7,0,0,0,289,306,3,40,20,8,290,291,10,6,0,0,
        291,292,7,1,0,0,292,306,3,40,20,7,293,294,10,5,0,0,294,295,7,2,0,
        0,295,306,3,40,20,6,296,297,10,4,0,0,297,298,7,3,0,0,298,306,3,40,
        20,5,299,300,10,3,0,0,300,301,5,42,0,0,301,306,3,40,20,4,302,303,
        10,2,0,0,303,304,5,43,0,0,304,306,3,40,20,3,305,287,1,0,0,0,305,
        290,1,0,0,0,305,293,1,0,0,0,305,296,1,0,0,0,305,299,1,0,0,0,305,
        302,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,
        41,1,0,0,0,309,307,1,0,0,0,310,319,5,50,0,0,311,319,5,52,0,0,312,
        319,5,53,0,0,313,319,3,26,13,0,314,315,5,54,0,0,315,316,3,40,20,
        0,316,317,5,55,0,0,317,319,1,0,0,0,318,310,1,0,0,0,318,311,1,0,0,
        0,318,312,1,0,0,0,318,313,1,0,0,0,318,314,1,0,0,0,319,43,1,0,0,0,
        320,321,7,4,0,0,321,45,1,0,0,0,31,48,51,53,67,80,88,100,108,120,
        128,137,145,153,162,170,178,182,187,197,200,219,230,235,241,265,
        270,274,277,305,307,318
    ]

class kmmszarpParser ( Parser ):

    grammarFileName = "kmmszarp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'p\\u0119tla'", "'zakres'", "'od'", "'do'", 
                     "'pocz\\u0105tek p\\u0119tli'", "'koniec p\\u0119tli'", 
                     "'podczas'", "'je\\u017Celi'", "'wtedy'", "'pocz\\u0105tek je\\u017Celi'", 
                     "'koniec je\\u017Celi'", "'w przeciwnym wypadku'", 
                     "'czynno\\u015B\\u0107'", "'parametry'", "'zwraca'", 
                     "'pocz\\u0105tek czynno\\u015Bci'", "'koniec czynno\\u015Bci'", 
                     "'i'", "'zmienna'", "'zwr\\u00F3\\u0107'", "'to'", 
                     "'tablica'", "'o d\\u0142ugo\\u015Bci'", "'we\\u017A'", 
                     "'element'", "'w\\u0142\\u00F3\\u017C'", "'na'", "'miejsce'", 
                     "'wywo\\u0142aj'", "'rzu\\u0107'", "'razy'", "'przez'", 
                     "'modu\\u0142'", "'doda\\u0107'", "'odj\\u0105\\u0107'", 
                     "'wi\\u0119ksze ni\\u017C'", "'mniejsze ni\\u017C'", 
                     "'wi\\u0119ksze lub r\\u00F3wne'", "'mniejsze lub r\\u00F3wne'", 
                     "'r\\u00F3wne'", "'nier\\u00F3wne'", "'oraz'", "'lub'", 
                     "'liczba'", "'napis'", "'prawdziwo\\u015B\\u0107'", 
                     "'nico\\u015B\\u0107'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'pocz\\u0105tek nawiasu'", 
                     "'koniec nawiasu'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "EXID", "ID", "INT", "PINT", "STRING", "BOOL", "LPAR", 
                      "RPAR", "WHITESPACE", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loopFor = 2
    RULE_loopWhile = 3
    RULE_conditionalStatement = 4
    RULE_conditionalStatementElse = 5
    RULE_functionDefinition = 6
    RULE_parameterList = 7
    RULE_parameter = 8
    RULE_returnStatement = 9
    RULE_variableDeclaration = 10
    RULE_arrayDeclaration = 11
    RULE_arrayValue = 12
    RULE_variableReference = 13
    RULE_arrayAccess = 14
    RULE_variableAssignment = 15
    RULE_arrayAssignment = 16
    RULE_functionCall = 17
    RULE_argumentList = 18
    RULE_cast = 19
    RULE_expression = 20
    RULE_primary = 21
    RULE_dtype = 22

    ruleNames =  [ "program", "statement", "loopFor", "loopWhile", "conditionalStatement", 
                   "conditionalStatementElse", "functionDefinition", "parameterList", 
                   "parameter", "returnStatement", "variableDeclaration", 
                   "arrayDeclaration", "arrayValue", "variableReference", 
                   "arrayAccess", "variableAssignment", "arrayAssignment", 
                   "functionCall", "argumentList", "cast", "expression", 
                   "primary", "dtype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    EXID=48
    ID=49
    INT=50
    PINT=51
    STRING=52
    BOOL=53
    LPAR=54
    RPAR=55
    WHITESPACE=56
    NEWLINE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def getRuleIndex(self):
            return kmmszarpParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = kmmszarpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144678139711725826) != 0):
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 8, 13, 19, 22, 26, 29, 30, 49]:
                    self.state = 46
                    self.statement()
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 47
                        self.match(kmmszarpParser.NEWLINE)


                    pass
                elif token in [57]:
                    self.state = 50
                    self.match(kmmszarpParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loopFor(self):
            return self.getTypedRuleContext(kmmszarpParser.LoopForContext,0)


        def loopWhile(self):
            return self.getTypedRuleContext(kmmszarpParser.LoopWhileContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(kmmszarpParser.ConditionalStatementContext,0)


        def conditionalStatementElse(self):
            return self.getTypedRuleContext(kmmszarpParser.ConditionalStatementElseContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(kmmszarpParser.FunctionDefinitionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(kmmszarpParser.VariableDeclarationContext,0)


        def arrayDeclaration(self):
            return self.getTypedRuleContext(kmmszarpParser.ArrayDeclarationContext,0)


        def variableAssignment(self):
            return self.getTypedRuleContext(kmmszarpParser.VariableAssignmentContext,0)


        def arrayAssignment(self):
            return self.getTypedRuleContext(kmmszarpParser.ArrayAssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(kmmszarpParser.FunctionCallContext,0)


        def cast(self):
            return self.getTypedRuleContext(kmmszarpParser.CastContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = kmmszarpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.loopFor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.loopWhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.conditionalStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.conditionalStatementElse()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.functionDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.variableDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.arrayDeclaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.variableAssignment()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.arrayAssignment()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 65
                self.functionCall()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 66
                self.cast()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(kmmszarpParser.VariableDeclarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_loopFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopFor" ):
                listener.enterLoopFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopFor" ):
                listener.exitLoopFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopFor" ):
                return visitor.visitLoopFor(self)
            else:
                return visitor.visitChildren(self)




    def loopFor(self):

        localctx = kmmszarpParser.LoopForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loopFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(kmmszarpParser.T__0)
            self.state = 70
            self.match(kmmszarpParser.T__1)
            self.state = 71
            self.variableDeclaration()
            self.state = 72
            self.match(kmmszarpParser.T__2)
            self.state = 73
            self.expression(0)
            self.state = 74
            self.match(kmmszarpParser.T__3)
            self.state = 75
            self.expression(0)
            self.state = 76
            self.match(kmmszarpParser.T__4)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 77
                self.match(kmmszarpParser.NEWLINE)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562951635869954) != 0):
                self.state = 83
                self.statement()
                self.state = 84
                self.match(kmmszarpParser.NEWLINE)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(kmmszarpParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_loopWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopWhile" ):
                listener.enterLoopWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopWhile" ):
                listener.exitLoopWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopWhile" ):
                return visitor.visitLoopWhile(self)
            else:
                return visitor.visitChildren(self)




    def loopWhile(self):

        localctx = kmmszarpParser.LoopWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loopWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(kmmszarpParser.T__0)
            self.state = 94
            self.match(kmmszarpParser.T__6)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.match(kmmszarpParser.T__4)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 97
                self.match(kmmszarpParser.NEWLINE)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562951635869954) != 0):
                self.state = 103
                self.statement()
                self.state = 104
                self.match(kmmszarpParser.NEWLINE)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(kmmszarpParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalStatement" ):
                return visitor.visitConditionalStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionalStatement(self):

        localctx = kmmszarpParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(kmmszarpParser.T__7)
            self.state = 114
            self.expression(0)
            self.state = 115
            self.match(kmmszarpParser.T__8)
            self.state = 116
            self.match(kmmszarpParser.T__9)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 117
                self.match(kmmszarpParser.NEWLINE)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562951635869954) != 0):
                self.state = 123
                self.statement()
                self.state = 124
                self.match(kmmszarpParser.NEWLINE)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(kmmszarpParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalStatement(self):
            return self.getTypedRuleContext(kmmszarpParser.ConditionalStatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_conditionalStatementElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatementElse" ):
                listener.enterConditionalStatementElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatementElse" ):
                listener.exitConditionalStatementElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalStatementElse" ):
                return visitor.visitConditionalStatementElse(self)
            else:
                return visitor.visitChildren(self)




    def conditionalStatementElse(self):

        localctx = kmmszarpParser.ConditionalStatementElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionalStatementElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.conditionalStatement()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 134
                self.match(kmmszarpParser.NEWLINE)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(kmmszarpParser.T__11)
            self.state = 141
            self.match(kmmszarpParser.T__9)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 142
                self.match(kmmszarpParser.NEWLINE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562951635869954) != 0):
                self.state = 148
                self.statement()
                self.state = 149
                self.match(kmmszarpParser.NEWLINE)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(kmmszarpParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(kmmszarpParser.ParameterListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(kmmszarpParser.NEWLINE)
            else:
                return self.getToken(kmmszarpParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.StatementContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.StatementContext,i)


        def returnStatement(self):
            return self.getTypedRuleContext(kmmszarpParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = kmmszarpParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(kmmszarpParser.T__12)
            self.state = 159
            self.match(kmmszarpParser.ID)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 160
                self.match(kmmszarpParser.T__13)
                self.state = 161
                self.parameterList()


            self.state = 164
            self.match(kmmszarpParser.T__14)
            self.state = 165
            self.dtype()
            self.state = 166
            self.match(kmmszarpParser.T__15)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 167
                    self.match(kmmszarpParser.NEWLINE) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562951635869954) != 0):
                self.state = 173
                self.statement()
                self.state = 174
                self.match(kmmszarpParser.NEWLINE)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 181
                self.returnStatement()


            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 184
                    self.match(kmmszarpParser.NEWLINE) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 190
            self.match(kmmszarpParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ParameterContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ParameterContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = kmmszarpParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 192
                self.parameter()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 193
                    self.match(kmmszarpParser.T__17)
                    self.state = 194
                    self.parameter()
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)


        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def getRuleIndex(self):
            return kmmszarpParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = kmmszarpParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(kmmszarpParser.T__18)
            self.state = 203
            self.dtype()
            self.state = 204
            self.match(kmmszarpParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = kmmszarpParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(kmmszarpParser.T__19)
            self.state = 207
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return kmmszarpParser.RULE_variableDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PureVariableDeclarationContext(VariableDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.VariableDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPureVariableDeclaration" ):
                listener.enterPureVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPureVariableDeclaration" ):
                listener.exitPureVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPureVariableDeclaration" ):
                return visitor.visitPureVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class VariableDeclarationWithAssignmentContext(VariableDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.VariableDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationWithAssignment" ):
                listener.enterVariableDeclarationWithAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationWithAssignment" ):
                listener.exitVariableDeclarationWithAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationWithAssignment" ):
                return visitor.visitVariableDeclarationWithAssignment(self)
            else:
                return visitor.visitChildren(self)



    def variableDeclaration(self):

        localctx = kmmszarpParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = kmmszarpParser.PureVariableDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(kmmszarpParser.T__18)
                self.state = 210
                self.dtype()
                self.state = 211
                self.match(kmmszarpParser.ID)
                pass

            elif la_ == 2:
                localctx = kmmszarpParser.VariableDeclarationWithAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(kmmszarpParser.T__18)
                self.state = 214
                self.dtype()
                self.state = 215
                self.match(kmmszarpParser.ID)
                self.state = 216
                self.match(kmmszarpParser.T__20)
                self.state = 217
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)


        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def arrayValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ArrayValueContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ArrayValueContext,i)


        def PINT(self):
            return self.getToken(kmmszarpParser.PINT, 0)

        def getRuleIndex(self):
            return kmmszarpParser.RULE_arrayDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclaration" ):
                listener.enterArrayDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclaration" ):
                listener.exitArrayDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclaration" ):
                return visitor.visitArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclaration(self):

        localctx = kmmszarpParser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(kmmszarpParser.T__21)
            self.state = 222
            self.dtype()
            self.state = 223
            self.match(kmmszarpParser.ID)
            self.state = 224
            self.match(kmmszarpParser.T__20)
            self.state = 225
            self.arrayValue()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 226
                self.match(kmmszarpParser.T__17)
                self.state = 227
                self.arrayValue()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 233
                self.match(kmmszarpParser.T__22)
                self.state = 234
                self.match(kmmszarpParser.PINT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_arrayValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = kmmszarpParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(kmmszarpParser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_variableReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableReference" ):
                listener.enterVariableReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableReference" ):
                listener.exitVariableReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableReference" ):
                return visitor.visitVariableReference(self)
            else:
                return visitor.visitChildren(self)




    def variableReference(self):

        localctx = kmmszarpParser.VariableReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variableReference)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(kmmszarpParser.ID)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.arrayAccess()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = kmmszarpParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(kmmszarpParser.T__23)
            self.state = 244
            self.expression(0)
            self.state = 245
            self.match(kmmszarpParser.T__24)
            self.state = 246
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_variableAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignment" ):
                listener.enterVariableAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignment" ):
                listener.exitVariableAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssignment" ):
                return visitor.visitVariableAssignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAssignment(self):

        localctx = kmmszarpParser.VariableAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(kmmszarpParser.ID)
            self.state = 249
            self.match(kmmszarpParser.T__20)
            self.state = 250
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_arrayAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignment" ):
                listener.enterArrayAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignment" ):
                listener.exitArrayAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignment" ):
                return visitor.visitArrayAssignment(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignment(self):

        localctx = kmmszarpParser.ArrayAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(kmmszarpParser.T__25)
            self.state = 253
            self.expression(0)
            self.state = 254
            self.match(kmmszarpParser.T__26)
            self.state = 255
            self.expression(0)
            self.state = 256
            self.match(kmmszarpParser.T__27)
            self.state = 257
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(kmmszarpParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(kmmszarpParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = kmmszarpParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(kmmszarpParser.T__28)
            self.state = 260
            self.match(kmmszarpParser.ID)
            self.state = 261
            self.argumentList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.VariableDeclarationContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = kmmszarpParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 265
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19]:
                    self.state = 263
                    self.variableDeclaration()
                    pass
                elif token in [24, 49, 50, 52, 53, 54]:
                    self.state = 264
                    self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 267
                    self.match(kmmszarpParser.T__17)
                    self.state = 270
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [19]:
                        self.state = 268
                        self.variableDeclaration()
                        pass
                    elif token in [24, 49, 50, 52, 53, 54]:
                        self.state = 269
                        self.expression(0)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)


        def dtype(self):
            return self.getTypedRuleContext(kmmszarpParser.DtypeContext,0)


        def getRuleIndex(self):
            return kmmszarpParser.RULE_cast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast" ):
                listener.enterCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast" ):
                listener.exitCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast" ):
                return visitor.visitCast(self)
            else:
                return visitor.visitChildren(self)




    def cast(self):

        localctx = kmmszarpParser.CastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(kmmszarpParser.T__29)
            self.state = 280
            self.expression(0)
            self.state = 281
            self.match(kmmszarpParser.T__26)
            self.state = 282
            self.dtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return kmmszarpParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.or_ = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class AdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(kmmszarpParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.eq = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)


    class LogicAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.ExpressionContext
            super().__init__(parser)
            self.and_ = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(kmmszarpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = kmmszarpParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = kmmszarpParser.PrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 285
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 305
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = kmmszarpParser.MultiplicationContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 287
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 288
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 289
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = kmmszarpParser.AdditionContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 290
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 291
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 292
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = kmmszarpParser.ComparisonContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 293
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 294
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 295
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = kmmszarpParser.EqualityContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 296
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 297
                        localctx.eq = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            localctx.eq = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 298
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = kmmszarpParser.LogicAndContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 299
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 300
                        localctx.and_ = self.match(kmmszarpParser.T__41)
                        self.state = 301
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = kmmszarpParser.LogicOrContext(self, kmmszarpParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 302
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 303
                        localctx.or_ = self.match(kmmszarpParser.T__42)
                        self.state = 304
                        self.expression(3)
                        pass

             
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return kmmszarpParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenthesizedExpressionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(kmmszarpParser.LPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(kmmszarpParser.ExpressionContext,0)

        def RPAR(self):
            return self.getToken(kmmszarpParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(kmmszarpParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(kmmszarpParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(kmmszarpParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class VariableReferencePrimaryContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a kmmszarpParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableReference(self):
            return self.getTypedRuleContext(kmmszarpParser.VariableReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableReferencePrimary" ):
                listener.enterVariableReferencePrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableReferencePrimary" ):
                listener.exitVariableReferencePrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableReferencePrimary" ):
                return visitor.visitVariableReferencePrimary(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = kmmszarpParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_primary)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                localctx = kmmszarpParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(kmmszarpParser.INT)
                pass
            elif token in [52]:
                localctx = kmmszarpParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.match(kmmszarpParser.STRING)
                pass
            elif token in [53]:
                localctx = kmmszarpParser.BoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.match(kmmszarpParser.BOOL)
                pass
            elif token in [24, 49]:
                localctx = kmmszarpParser.VariableReferencePrimaryContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.variableReference()
                pass
            elif token in [54]:
                localctx = kmmszarpParser.ParenthesizedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.match(kmmszarpParser.LPAR)
                self.state = 315
                self.expression(0)
                self.state = 316
                self.match(kmmszarpParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return kmmszarpParser.RULE_dtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtype" ):
                listener.enterDtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtype" ):
                listener.exitDtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDtype" ):
                return visitor.visitDtype(self)
            else:
                return visitor.visitChildren(self)




    def dtype(self):

        localctx = kmmszarpParser.DtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 263882790666240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




