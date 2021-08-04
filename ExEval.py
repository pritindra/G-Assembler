# evaluator

import sys
import tokenizer as tok
import symbols

class ExEval:
    def __init__(self, token):
        self.initOperations()
        self.parse(token)

    def __init__( self, token ):
        self.initOperators()
        self.parse( token )

    def doPushConst( self ):
        self.m_stack.append( self.m_postfix[ self.m_index] )
        self.m_index = self.m_index + 1

    def doPushSym( self ):
        symbol = self.m_postfix[ self.m_index]
        self.m_index = self.m_index + 1

        if symbols.isDefined( symbol ):
            self.m_stack.append( symbols.get( symbol ) )
        else:
            self.m_undefined = True
            self.m_stack.append( 1 )

    def Add(self):
        v1 = self.m_stack.pop()
        v2 = self.m_stack.pop()
        self.m_stack.append(v2 + v1)

    def And(self):
        v1 = self.m_stack.pop()
        v2 = self.m_stack.pop()
        self.m_stack.append(v2 & v1)
    
    def Div(self):
        v1 = self.m_stack.pop()
        v2 = self.m_stack.pop()
        if v1 == 0:
            raise Exception("divison by zero")
        self.m_stack.append(v2 / v1)
    
    def Mul(self):
        v1 = self.m_stack.pop()
        v2 = self.m_stack.pop()
        self.m_stack.append(v2 * v1)
    
    def Xor(self):
        v1 = self.m_stack.pop()
        v2 = self.m_stack.pop()
        self.m_stack.append(v2 ^ v1)

    def eval(self):
        self.m_stack = []
        self.m_index = []

        assert len(self.m_stack) == 1

    def initOps(self):
        self.m_operators = [
            {'&': self.And, '^': self.Xor},
            {'+': self.Add },
            {'/': self.div, '*': self.Mul}
        ]

    def parse(self, token):
        if token.curTok() == tok.SYMBOL:
            self.m_postfix.append(self.doPushSym)
            self.m_postfix.append(token.curValue())
            token.nextTok()

        elif token.curTok() == tok.NUMBER:
            self.m_postfix.append(self.doPushConst)
            self.m_postfix.append(token.curValue())
            token.nextTok()

        elif token.curTok() == tok.STRING:
            if len(token.curValue()) != 1:
                raise Exception ('String must be one character')
            self.m_postfix.append(self.doPushConst)
            self.m_postfix.append(ord(token.curValue()[0]))
            token.nextTok()

        else:
            raise Exception(str.format("unexpected token {0}", token.curTok()))
    self.m_postfix = []
    
