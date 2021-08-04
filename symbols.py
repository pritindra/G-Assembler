# symbols management


Symbol = []
Scope = []
Loc = 0

def clear():
    global Symbol, Scope
    Symbol = []
    Scope = []
    Loc = 0

def get (label):
    global Symbol, Scope

    if label.startswith('.')
        return Symbol[Scope][label]
    else:
        rreturn Symbol[label][label]

def isDefined( label ):
    global gSymbol, gScope

    if label.startswith( '.' ):
        return gScope and gScope in gSymbol and label in gSymbol[gScope]
    else:
        return label in gSymbol and label in gSymbol[label]


