from sympy import sin, cos, tan, log

tokens = (
    'VAR',
    'FUNC_VAR',
    'NUMBER',
    'BUILD_IN_FUNC',
    'CONSTANTS',
    'LIMIT_SYM',
    'R_ARROW'
)

literals = ['=','+','-','*','/', '^', '(',')', ',', 'd', 'S', '[', ']']

t_VAR = r'(?!(sin|cos|tan|log|oo|pi|lim))[abcijklmnpqrstuvwxyz]'
t_FUNC_VAR = r'[f-h]'
t_CONSTANTS = r'(oo|pi|e)'
t_LIMIT_SYM = r'lim'
t_R_ARROW = r'->'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BUILD_IN_FUNC(t):
    r'(sin|cos|tan|log)'
    t.value = eval(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()
