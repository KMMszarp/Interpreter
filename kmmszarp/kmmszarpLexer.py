# Generated from ./kmmszarp.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,61,715,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,
        1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,
        1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,
        1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,
        1,50,1,50,1,50,1,51,1,51,1,51,5,51,570,8,51,10,51,12,51,573,9,51,
        1,52,1,52,1,52,1,52,1,52,3,52,580,8,52,1,52,4,52,583,8,52,11,52,
        12,52,584,1,53,4,53,588,8,53,11,53,12,53,589,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,54,5,54,613,8,54,10,54,12,54,616,9,54,1,54,1,54,
        1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,
        1,55,1,55,1,55,1,55,3,55,650,8,55,1,56,1,56,1,56,1,56,1,56,1,56,
        1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,57,1,57,
        1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,
        1,58,4,58,685,8,58,11,58,12,58,686,1,58,1,58,1,59,3,59,692,8,59,
        1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,60,5,60,702,8,60,10,60,12,60,
        705,9,60,1,60,1,60,1,61,1,61,1,62,3,62,712,8,62,1,63,1,63,0,0,64,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,
        49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,
        71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,
        93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,
        113,57,115,58,117,59,119,60,121,61,123,0,125,0,127,0,1,0,4,2,0,10,
        10,13,13,2,0,9,9,32,32,10,0,65,90,211,211,260,260,262,262,280,280,
        321,321,323,323,346,346,377,377,379,379,9,0,65,90,97,122,211,211,
        243,243,260,263,280,281,321,324,346,347,377,380,721,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,
        1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,
        1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,
        1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,
        1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,
        1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,
        1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,
        1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,
        0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,
        0,0,0,1,129,1,0,0,0,3,135,1,0,0,0,5,142,1,0,0,0,7,145,1,0,0,0,9,
        148,1,0,0,0,11,163,1,0,0,0,13,176,1,0,0,0,15,184,1,0,0,0,17,191,
        1,0,0,0,19,197,1,0,0,0,21,213,1,0,0,0,23,227,1,0,0,0,25,248,1,0,
        0,0,27,257,1,0,0,0,29,267,1,0,0,0,31,274,1,0,0,0,33,293,1,0,0,0,
        35,310,1,0,0,0,37,312,1,0,0,0,39,320,1,0,0,0,41,326,1,0,0,0,43,329,
        1,0,0,0,45,337,1,0,0,0,47,348,1,0,0,0,49,352,1,0,0,0,51,360,1,0,
        0,0,53,365,1,0,0,0,55,368,1,0,0,0,57,376,1,0,0,0,59,384,1,0,0,0,
        61,389,1,0,0,0,63,394,1,0,0,0,65,400,1,0,0,0,67,406,1,0,0,0,69,412,
        1,0,0,0,71,418,1,0,0,0,73,430,1,0,0,0,75,443,1,0,0,0,77,461,1,0,
        0,0,79,480,1,0,0,0,81,489,1,0,0,0,83,497,1,0,0,0,85,501,1,0,0,0,
        87,507,1,0,0,0,89,516,1,0,0,0,91,521,1,0,0,0,93,525,1,0,0,0,95,532,
        1,0,0,0,97,538,1,0,0,0,99,550,1,0,0,0,101,557,1,0,0,0,103,566,1,
        0,0,0,105,579,1,0,0,0,107,587,1,0,0,0,109,591,1,0,0,0,111,649,1,
        0,0,0,113,651,1,0,0,0,115,668,1,0,0,0,117,684,1,0,0,0,119,691,1,
        0,0,0,121,695,1,0,0,0,123,708,1,0,0,0,125,711,1,0,0,0,127,713,1,
        0,0,0,129,130,5,112,0,0,130,131,5,281,0,0,131,132,5,116,0,0,132,
        133,5,108,0,0,133,134,5,97,0,0,134,2,1,0,0,0,135,136,5,122,0,0,136,
        137,5,97,0,0,137,138,5,107,0,0,138,139,5,114,0,0,139,140,5,101,0,
        0,140,141,5,115,0,0,141,4,1,0,0,0,142,143,5,111,0,0,143,144,5,100,
        0,0,144,6,1,0,0,0,145,146,5,100,0,0,146,147,5,111,0,0,147,8,1,0,
        0,0,148,149,5,112,0,0,149,150,5,111,0,0,150,151,5,99,0,0,151,152,
        5,122,0,0,152,153,5,261,0,0,153,154,5,116,0,0,154,155,5,101,0,0,
        155,156,5,107,0,0,156,157,5,32,0,0,157,158,5,112,0,0,158,159,5,281,
        0,0,159,160,5,116,0,0,160,161,5,108,0,0,161,162,5,105,0,0,162,10,
        1,0,0,0,163,164,5,107,0,0,164,165,5,111,0,0,165,166,5,110,0,0,166,
        167,5,105,0,0,167,168,5,101,0,0,168,169,5,99,0,0,169,170,5,32,0,
        0,170,171,5,112,0,0,171,172,5,281,0,0,172,173,5,116,0,0,173,174,
        5,108,0,0,174,175,5,105,0,0,175,12,1,0,0,0,176,177,5,112,0,0,177,
        178,5,111,0,0,178,179,5,100,0,0,179,180,5,99,0,0,180,181,5,122,0,
        0,181,182,5,97,0,0,182,183,5,115,0,0,183,14,1,0,0,0,184,185,5,106,
        0,0,185,186,5,101,0,0,186,187,5,380,0,0,187,188,5,101,0,0,188,189,
        5,108,0,0,189,190,5,105,0,0,190,16,1,0,0,0,191,192,5,119,0,0,192,
        193,5,116,0,0,193,194,5,101,0,0,194,195,5,100,0,0,195,196,5,121,
        0,0,196,18,1,0,0,0,197,198,5,112,0,0,198,199,5,111,0,0,199,200,5,
        99,0,0,200,201,5,122,0,0,201,202,5,261,0,0,202,203,5,116,0,0,203,
        204,5,101,0,0,204,205,5,107,0,0,205,206,5,32,0,0,206,207,5,106,0,
        0,207,208,5,101,0,0,208,209,5,380,0,0,209,210,5,101,0,0,210,211,
        5,108,0,0,211,212,5,105,0,0,212,20,1,0,0,0,213,214,5,107,0,0,214,
        215,5,111,0,0,215,216,5,110,0,0,216,217,5,105,0,0,217,218,5,101,
        0,0,218,219,5,99,0,0,219,220,5,32,0,0,220,221,5,106,0,0,221,222,
        5,101,0,0,222,223,5,380,0,0,223,224,5,101,0,0,224,225,5,108,0,0,
        225,226,5,105,0,0,226,22,1,0,0,0,227,228,5,119,0,0,228,229,5,32,
        0,0,229,230,5,112,0,0,230,231,5,114,0,0,231,232,5,122,0,0,232,233,
        5,101,0,0,233,234,5,99,0,0,234,235,5,105,0,0,235,236,5,119,0,0,236,
        237,5,110,0,0,237,238,5,121,0,0,238,239,5,109,0,0,239,240,5,32,0,
        0,240,241,5,119,0,0,241,242,5,121,0,0,242,243,5,112,0,0,243,244,
        5,97,0,0,244,245,5,100,0,0,245,246,5,107,0,0,246,247,5,117,0,0,247,
        24,1,0,0,0,248,249,5,99,0,0,249,250,5,122,0,0,250,251,5,121,0,0,
        251,252,5,110,0,0,252,253,5,110,0,0,253,254,5,111,0,0,254,255,5,
        347,0,0,255,256,5,263,0,0,256,26,1,0,0,0,257,258,5,112,0,0,258,259,
        5,97,0,0,259,260,5,114,0,0,260,261,5,97,0,0,261,262,5,109,0,0,262,
        263,5,101,0,0,263,264,5,116,0,0,264,265,5,114,0,0,265,266,5,121,
        0,0,266,28,1,0,0,0,267,268,5,122,0,0,268,269,5,119,0,0,269,270,5,
        114,0,0,270,271,5,97,0,0,271,272,5,99,0,0,272,273,5,97,0,0,273,30,
        1,0,0,0,274,275,5,112,0,0,275,276,5,111,0,0,276,277,5,99,0,0,277,
        278,5,122,0,0,278,279,5,261,0,0,279,280,5,116,0,0,280,281,5,101,
        0,0,281,282,5,107,0,0,282,283,5,32,0,0,283,284,5,99,0,0,284,285,
        5,122,0,0,285,286,5,121,0,0,286,287,5,110,0,0,287,288,5,110,0,0,
        288,289,5,111,0,0,289,290,5,347,0,0,290,291,5,99,0,0,291,292,5,105,
        0,0,292,32,1,0,0,0,293,294,5,107,0,0,294,295,5,111,0,0,295,296,5,
        110,0,0,296,297,5,105,0,0,297,298,5,101,0,0,298,299,5,99,0,0,299,
        300,5,32,0,0,300,301,5,99,0,0,301,302,5,122,0,0,302,303,5,121,0,
        0,303,304,5,110,0,0,304,305,5,110,0,0,305,306,5,111,0,0,306,307,
        5,347,0,0,307,308,5,99,0,0,308,309,5,105,0,0,309,34,1,0,0,0,310,
        311,5,105,0,0,311,36,1,0,0,0,312,313,5,122,0,0,313,314,5,109,0,0,
        314,315,5,105,0,0,315,316,5,101,0,0,316,317,5,110,0,0,317,318,5,
        110,0,0,318,319,5,97,0,0,319,38,1,0,0,0,320,321,5,122,0,0,321,322,
        5,119,0,0,322,323,5,114,0,0,323,324,5,243,0,0,324,325,5,263,0,0,
        325,40,1,0,0,0,326,327,5,116,0,0,327,328,5,111,0,0,328,42,1,0,0,
        0,329,330,5,116,0,0,330,331,5,97,0,0,331,332,5,98,0,0,332,333,5,
        108,0,0,333,334,5,105,0,0,334,335,5,99,0,0,335,336,5,97,0,0,336,
        44,1,0,0,0,337,338,5,111,0,0,338,339,5,32,0,0,339,340,5,100,0,0,
        340,341,5,322,0,0,341,342,5,117,0,0,342,343,5,103,0,0,343,344,5,
        111,0,0,344,345,5,347,0,0,345,346,5,99,0,0,346,347,5,105,0,0,347,
        46,1,0,0,0,348,349,5,119,0,0,349,350,5,101,0,0,350,351,5,378,0,0,
        351,48,1,0,0,0,352,353,5,101,0,0,353,354,5,108,0,0,354,355,5,101,
        0,0,355,356,5,109,0,0,356,357,5,101,0,0,357,358,5,110,0,0,358,359,
        5,116,0,0,359,50,1,0,0,0,360,361,5,119,0,0,361,362,5,322,0,0,362,
        363,5,243,0,0,363,364,5,380,0,0,364,52,1,0,0,0,365,366,5,110,0,0,
        366,367,5,97,0,0,367,54,1,0,0,0,368,369,5,109,0,0,369,370,5,105,
        0,0,370,371,5,101,0,0,371,372,5,106,0,0,372,373,5,115,0,0,373,374,
        5,99,0,0,374,375,5,101,0,0,375,56,1,0,0,0,376,377,5,119,0,0,377,
        378,5,121,0,0,378,379,5,119,0,0,379,380,5,111,0,0,380,381,5,322,
        0,0,381,382,5,97,0,0,382,383,5,106,0,0,383,58,1,0,0,0,384,385,5,
        114,0,0,385,386,5,122,0,0,386,387,5,117,0,0,387,388,5,263,0,0,388,
        60,1,0,0,0,389,390,5,114,0,0,390,391,5,97,0,0,391,392,5,122,0,0,
        392,393,5,121,0,0,393,62,1,0,0,0,394,395,5,112,0,0,395,396,5,114,
        0,0,396,397,5,122,0,0,397,398,5,101,0,0,398,399,5,122,0,0,399,64,
        1,0,0,0,400,401,5,109,0,0,401,402,5,111,0,0,402,403,5,100,0,0,403,
        404,5,117,0,0,404,405,5,322,0,0,405,66,1,0,0,0,406,407,5,100,0,0,
        407,408,5,111,0,0,408,409,5,100,0,0,409,410,5,97,0,0,410,411,5,263,
        0,0,411,68,1,0,0,0,412,413,5,111,0,0,413,414,5,100,0,0,414,415,5,
        106,0,0,415,416,5,261,0,0,416,417,5,263,0,0,417,70,1,0,0,0,418,419,
        5,119,0,0,419,420,5,105,0,0,420,421,5,281,0,0,421,422,5,107,0,0,
        422,423,5,115,0,0,423,424,5,122,0,0,424,425,5,101,0,0,425,426,5,
        32,0,0,426,427,5,110,0,0,427,428,5,105,0,0,428,429,5,380,0,0,429,
        72,1,0,0,0,430,431,5,109,0,0,431,432,5,110,0,0,432,433,5,105,0,0,
        433,434,5,101,0,0,434,435,5,106,0,0,435,436,5,115,0,0,436,437,5,
        122,0,0,437,438,5,101,0,0,438,439,5,32,0,0,439,440,5,110,0,0,440,
        441,5,105,0,0,441,442,5,380,0,0,442,74,1,0,0,0,443,444,5,119,0,0,
        444,445,5,105,0,0,445,446,5,281,0,0,446,447,5,107,0,0,447,448,5,
        115,0,0,448,449,5,122,0,0,449,450,5,101,0,0,450,451,5,32,0,0,451,
        452,5,108,0,0,452,453,5,117,0,0,453,454,5,98,0,0,454,455,5,32,0,
        0,455,456,5,114,0,0,456,457,5,243,0,0,457,458,5,119,0,0,458,459,
        5,110,0,0,459,460,5,101,0,0,460,76,1,0,0,0,461,462,5,109,0,0,462,
        463,5,110,0,0,463,464,5,105,0,0,464,465,5,101,0,0,465,466,5,106,
        0,0,466,467,5,115,0,0,467,468,5,122,0,0,468,469,5,101,0,0,469,470,
        5,32,0,0,470,471,5,108,0,0,471,472,5,117,0,0,472,473,5,98,0,0,473,
        474,5,32,0,0,474,475,5,114,0,0,475,476,5,243,0,0,476,477,5,119,0,
        0,477,478,5,110,0,0,478,479,5,101,0,0,479,78,1,0,0,0,480,481,5,112,
        0,0,481,482,5,114,0,0,482,483,5,122,0,0,483,484,5,101,0,0,484,485,
        5,109,0,0,485,486,5,105,0,0,486,487,5,101,0,0,487,488,5,324,0,0,
        488,80,1,0,0,0,489,490,5,122,0,0,490,491,5,97,0,0,491,492,5,110,
        0,0,492,493,5,101,0,0,493,494,5,103,0,0,494,495,5,117,0,0,495,496,
        5,106,0,0,496,82,1,0,0,0,497,498,5,110,0,0,498,499,5,105,0,0,499,
        500,5,101,0,0,500,84,1,0,0,0,501,502,5,114,0,0,502,503,5,243,0,0,
        503,504,5,119,0,0,504,505,5,110,0,0,505,506,5,101,0,0,506,86,1,0,
        0,0,507,508,5,110,0,0,508,509,5,105,0,0,509,510,5,101,0,0,510,511,
        5,114,0,0,511,512,5,243,0,0,512,513,5,119,0,0,513,514,5,110,0,0,
        514,515,5,101,0,0,515,88,1,0,0,0,516,517,5,111,0,0,517,518,5,114,
        0,0,518,519,5,97,0,0,519,520,5,122,0,0,520,90,1,0,0,0,521,522,5,
        108,0,0,522,523,5,117,0,0,523,524,5,98,0,0,524,92,1,0,0,0,525,526,
        5,108,0,0,526,527,5,105,0,0,527,528,5,99,0,0,528,529,5,122,0,0,529,
        530,5,98,0,0,530,531,5,97,0,0,531,94,1,0,0,0,532,533,5,110,0,0,533,
        534,5,97,0,0,534,535,5,112,0,0,535,536,5,105,0,0,536,537,5,115,0,
        0,537,96,1,0,0,0,538,539,5,112,0,0,539,540,5,114,0,0,540,541,5,97,
        0,0,541,542,5,119,0,0,542,543,5,100,0,0,543,544,5,122,0,0,544,545,
        5,105,0,0,545,546,5,119,0,0,546,547,5,111,0,0,547,548,5,347,0,0,
        548,549,5,263,0,0,549,98,1,0,0,0,550,551,5,110,0,0,551,552,5,105,
        0,0,552,553,5,99,0,0,553,554,5,111,0,0,554,555,5,347,0,0,555,556,
        5,263,0,0,556,100,1,0,0,0,557,558,5,111,0,0,558,559,5,100,0,0,559,
        560,5,107,0,0,560,561,5,114,0,0,561,562,5,121,0,0,562,563,5,106,
        0,0,563,564,1,0,0,0,564,565,3,103,51,0,565,102,1,0,0,0,566,571,3,
        123,61,0,567,570,3,123,61,0,568,570,3,127,63,0,569,567,1,0,0,0,569,
        568,1,0,0,0,570,573,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,
        104,1,0,0,0,573,571,1,0,0,0,574,575,5,109,0,0,575,576,5,105,0,0,
        576,577,5,110,0,0,577,578,5,117,0,0,578,580,5,115,0,0,579,574,1,
        0,0,0,579,580,1,0,0,0,580,582,1,0,0,0,581,583,3,127,63,0,582,581,
        1,0,0,0,583,584,1,0,0,0,584,582,1,0,0,0,584,585,1,0,0,0,585,106,
        1,0,0,0,586,588,3,127,63,0,587,586,1,0,0,0,588,589,1,0,0,0,589,587,
        1,0,0,0,589,590,1,0,0,0,590,108,1,0,0,0,591,592,5,112,0,0,592,593,
        5,111,0,0,593,594,5,99,0,0,594,595,5,122,0,0,595,596,5,261,0,0,596,
        597,5,116,0,0,597,598,5,101,0,0,598,599,5,107,0,0,599,600,5,32,0,
        0,600,601,5,99,0,0,601,602,5,117,0,0,602,603,5,100,0,0,603,604,5,
        122,0,0,604,605,5,121,0,0,605,606,5,115,0,0,606,607,5,322,0,0,607,
        608,5,111,0,0,608,609,5,119,0,0,609,610,5,117,0,0,610,614,1,0,0,
        0,611,613,8,0,0,0,612,611,1,0,0,0,613,616,1,0,0,0,614,612,1,0,0,
        0,614,615,1,0,0,0,615,617,1,0,0,0,616,614,1,0,0,0,617,618,5,107,
        0,0,618,619,5,111,0,0,619,620,5,110,0,0,620,621,5,105,0,0,621,622,
        5,101,0,0,622,623,5,99,0,0,623,624,5,32,0,0,624,625,5,99,0,0,625,
        626,5,117,0,0,626,627,5,100,0,0,627,628,5,122,0,0,628,629,5,121,
        0,0,629,630,5,115,0,0,630,631,5,322,0,0,631,632,5,111,0,0,632,633,
        5,119,0,0,633,634,5,117,0,0,634,110,1,0,0,0,635,636,5,112,0,0,636,
        637,5,114,0,0,637,638,5,97,0,0,638,639,5,119,0,0,639,640,5,100,0,
        0,640,650,5,97,0,0,641,642,5,107,0,0,642,643,5,322,0,0,643,644,5,
        97,0,0,644,645,5,109,0,0,645,646,5,115,0,0,646,647,5,116,0,0,647,
        648,5,119,0,0,648,650,5,111,0,0,649,635,1,0,0,0,649,641,1,0,0,0,
        650,112,1,0,0,0,651,652,5,112,0,0,652,653,5,111,0,0,653,654,5,99,
        0,0,654,655,5,122,0,0,655,656,5,261,0,0,656,657,5,116,0,0,657,658,
        5,101,0,0,658,659,5,107,0,0,659,660,5,32,0,0,660,661,5,110,0,0,661,
        662,5,97,0,0,662,663,5,119,0,0,663,664,5,105,0,0,664,665,5,97,0,
        0,665,666,5,115,0,0,666,667,5,117,0,0,667,114,1,0,0,0,668,669,5,
        107,0,0,669,670,5,111,0,0,670,671,5,110,0,0,671,672,5,105,0,0,672,
        673,5,101,0,0,673,674,5,99,0,0,674,675,5,32,0,0,675,676,5,110,0,
        0,676,677,5,97,0,0,677,678,5,119,0,0,678,679,5,105,0,0,679,680,5,
        97,0,0,680,681,5,115,0,0,681,682,5,117,0,0,682,116,1,0,0,0,683,685,
        7,1,0,0,684,683,1,0,0,0,685,686,1,0,0,0,686,684,1,0,0,0,686,687,
        1,0,0,0,687,688,1,0,0,0,688,689,6,58,0,0,689,118,1,0,0,0,690,692,
        5,13,0,0,691,690,1,0,0,0,691,692,1,0,0,0,692,693,1,0,0,0,693,694,
        5,10,0,0,694,120,1,0,0,0,695,696,5,111,0,0,696,697,5,112,0,0,697,
        698,5,105,0,0,698,699,5,115,0,0,699,703,1,0,0,0,700,702,8,0,0,0,
        701,700,1,0,0,0,702,705,1,0,0,0,703,701,1,0,0,0,703,704,1,0,0,0,
        704,706,1,0,0,0,705,703,1,0,0,0,706,707,6,60,0,0,707,122,1,0,0,0,
        708,709,7,2,0,0,709,124,1,0,0,0,710,712,7,3,0,0,711,710,1,0,0,0,
        712,126,1,0,0,0,713,714,2,48,57,0,714,128,1,0,0,0,12,0,569,571,579,
        584,589,614,649,686,691,703,711,1,6,0,0
    ]

class kmmszarpLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    EXID = 51
    ID = 52
    INT = 53
    PINT = 54
    STRING = 55
    BOOL = 56
    LPAR = 57
    RPAR = 58
    WHITESPACE = 59
    NEWLINE = 60
    COMMENT = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'p\\u0119tla'", "'zakres'", "'od'", "'do'", "'pocz\\u0105tek p\\u0119tli'", 
            "'koniec p\\u0119tli'", "'podczas'", "'je\\u017Celi'", "'wtedy'", 
            "'pocz\\u0105tek je\\u017Celi'", "'koniec je\\u017Celi'", "'w przeciwnym wypadku'", 
            "'czynno\\u015B\\u0107'", "'parametry'", "'zwraca'", "'pocz\\u0105tek czynno\\u015Bci'", 
            "'koniec czynno\\u015Bci'", "'i'", "'zmienna'", "'zwr\\u00F3\\u0107'", 
            "'to'", "'tablica'", "'o d\\u0142ugo\\u015Bci'", "'we\\u017A'", 
            "'element'", "'w\\u0142\\u00F3\\u017C'", "'na'", "'miejsce'", 
            "'wywo\\u0142aj'", "'rzu\\u0107'", "'razy'", "'przez'", "'modu\\u0142'", 
            "'doda\\u0107'", "'odj\\u0105\\u0107'", "'wi\\u0119ksze ni\\u017C'", 
            "'mniejsze ni\\u017C'", "'wi\\u0119ksze lub r\\u00F3wne'", "'mniejsze lub r\\u00F3wne'", 
            "'przemie\\u0144'", "'zaneguj'", "'nie'", "'r\\u00F3wne'", "'nier\\u00F3wne'", 
            "'oraz'", "'lub'", "'liczba'", "'napis'", "'prawdziwo\\u015B\\u0107'", 
            "'nico\\u015B\\u0107'", "'pocz\\u0105tek nawiasu'", "'koniec nawiasu'" ]

    symbolicNames = [ "<INVALID>",
            "EXID", "ID", "INT", "PINT", "STRING", "BOOL", "LPAR", "RPAR", 
            "WHITESPACE", "NEWLINE", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "EXID", "ID", "INT", "PINT", "STRING", "BOOL", "LPAR", 
                  "RPAR", "WHITESPACE", "NEWLINE", "COMMENT", "ULETTER", 
                  "LETTER", "DIGIT" ]

    grammarFileName = "kmmszarp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


