"""
This file contains the function to transform the source code and make 
a compliant python script. 
"""

import tokenize

def pytwister_tokenize(readline):
    """
    this function tokenizes readline (which is the readline method of
    a file or StringIO object, and transforms the script into a 
    compliant python source. It gives back a list of compliant tokens, 
    that later can be untokenize (by tokenize.untokenize) to produce
    python source code to be compiled. 
    """
    
    indent = 4
    curindent = 0
    curpos = 0

    tokens = tokenize.generate_tokens(readline)
   
    newtoks = list()
    prevtok = None
    try:
        for tok in tokens:
            skiptok = False
            curtype, curstr, curstart, curend, curline = tok
            toklen = curend[1] - curstart[1]
            curstart = (curstart[0], curindent + curpos)
            curend = (curend[0], curindent + curpos + toklen)
            
            curpos += toklen + 1
            
            if curtype == tokenize.OP:
                if curstr == "-" and prevtok.string == "<" and prevtok and tok.start[1] == prevtok.end[1]:
                    newtoks.pop()
                    newtok = tokenize.TokenInfo(tokenize.OP, "=", curstart, curend, curline)
                else:
                    newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
            elif (curtype == tokenize.NL or curtype == tokenize.NEWLINE) and prevtok and prevtok.type == tokenize.OP:
                if prevtok.string == "{":
                    newtoks.pop()
                    newtoks.append(tokenize.TokenInfo(tokenize.OP, ":", prevtok.start, prevtok.end, prevtok.line))
                    newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
                    curindent += indent
                    curpos = 0
                if prevtok.string == "}" and (newtoks[-2].type == tokenize.NL or newtoks[-2].type == tokenize.NEWLINE):
                    newtoks.pop()
                    newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
                    curindent -= indent
                    curpos = 0
                else:
                    newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
                    curpos = 0
            elif curtype == tokenize.NL or curtype == tokenize.NEWLINE or curtype == tokenize.ENCODING:
                newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
                curpos = 0
            elif tok.type == tokenize.NAME and tok.string == "function":
                if newtoks[-1].type == tokenize.OP and newtoks[-1].string == "=":
                    funname = newtoks[-2]
                    newtoks.pop()
                    newtoks.pop()
                    curline = funname.start[0]
                    newstart = funname.start[1]
                    newtoks.append(tokenize.TokenInfo(tokenize.NAME, "def", (curline, curindent + newstart), (curline, curindent + newstart + 3), curline))
                    newstart += 4
                    newtok = tokenize.TokenInfo(tokenize.NAME, funname.string, (curline, curindent + newstart), (curline, curindent + newstart + len(funname.string)), curline)
                    curpos = newstart + len(funname.string) + 1
            else:
                newtok = tokenize.TokenInfo(curtype, curstr, curstart, curend, curline)
            
            newtoks.append(newtok)
            prevtok = newtok
    except tokenize.TokenError as e:
        if "EOF in multi-line statement" in str(e):
            pass

    return newtoks
