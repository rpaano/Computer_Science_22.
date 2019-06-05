#Name: Romel Niño O. Paano
#Section: CSA 


##Main 0.5
with open('file.txt') as f:
    strings = [line.rstrip() for line in f]
counter = strings[0]
string = strings[1]
token = []
more = []
sente = []
ctr1 = 0
let = 0
ctr = 2



#tokenizer with a bit of parsering
def Tokenizer(string):
    ctr = 0
    if string[0] != 'A' and string[0] != 'B' and string[0] != 'C':
        return 1
    while ctr != len(string):
        if string[ctr] == 'A' or string[ctr] == 'B' or string[ctr] == 'C':
            num1 = "id"
            token.append(num1)
            ctr += 1
        elif string[ctr].isdigit():
            while string[ctr].isdigit():
                ctr+=1
                if ctr == len(string):
                    break
            token.append("id")
        elif string[ctr] == '+':
            token.append("+")
            ctr += 1
        elif string[ctr] == '-':
            token.append("-")
            ctr += 1
        elif string[ctr] == '*':
            token.append("*")
            ctr += 1
        elif string[ctr] == '/':
            token.append("/")
            ctr += 1
        elif string[ctr] == '=':
            token.append("=")
            ctr += 1
        elif string[ctr] == '(':
            token.append("(")
            ctr += 1
        elif string[ctr] == ')':
            token.append(")")
            ctr += 1
        elif string[ctr] == ' ':
            ctr += 1
        else:
            return 1
            break
    return token

def moreToken(token):
    length = 0
    while length != len(token):
        if token[length] == '+':
            more.append('+')
            length += 1
        elif token[length] == '-':
            more.append('-')
            length += 1
        elif token[length] == '*':
            more.append('*')
            length += 1
        elif token[length] == '/':
            more.append('/')
            length += 1
        elif token[length] == '(':
            more.append('(')
            length += 1
        elif token[length] == ')':
            more.append(')')
            length += 1
        elif token[length] == '=':
            more.append('=')
            length += 1
        else:
            length += 1
    return more

def assign():
    sente.append("id")
    sente.append("=")
    sente.append("expr")
    if let == len(more):
        return sente
    if more[let] == '+' or more[let] == '-' or more[let] == '*' or more[let] == '/' or more[let] == '(':
        return expr()
    else:
        return 1

def expr():
    global let
    count = 0
    ctr = len(sente)-1
    if more[let] == '+' or more[let] == '-':
        while more[let] == '+' or more[let] == '-':
            count += 1
            let += 1
            if let == len(more):
                break
        count2 = count
        let -= 1
        while count != 0:
            if more[let] == '+':
                sente[ctr] = 'expr'
                sente.insert(ctr+1,'+')
                sente.insert(ctr+2,'term')
                count -= 1
                let -= 1
            elif more[let] == '-':
                sente[ctr] = 'expr'
                sente.insert(ctr+1,'-')
                sente.insert(ctr+2,'term')
                count -= 1
                let -= 1
        let += count2
        let += 1
        ## check if out of range
        if let >= len(more):
            return sente
        if more[let] == '*' or more[let] == '/' or more[let] == '(':
            return term()
        elif more[let] == ')':
            sente.append(")")
            let += 1
            if let != len(more):
                return term()
    elif more[let] == '*' or more[let] == '/' or more[let] == '(':
        return term()
    else:
        return 1
    
def term():
    global let
    count = 0    
    ctr2 = len(sente)-1
    if more[let] == '*' or more[let] == '/':
        while more[let] == '*' or more[let] == '/':
            count += 1
            let += 1
            if let == len(more):
                break
        count2 = count
        let -= 1
        while count != 0:
            if more[let] == '*':
                if sente[ctr2] == ")":
                    sente.append("*")
                    sente.append("factor")
                else:
                    sente[ctr2]= 'term'
                    sente.insert(ctr2+1,'*')
                    sente.insert(ctr2+2,'factor')
                count -= 1
                let -= 1
            elif more[let] == '/':
                if sente[ctr2] == ")":
                    sente.append("/")
                    sente.append("factor")
                else:
                    sente[ctr2]= 'term'
                    sente.insert(ctr2+1,'/')
                    sente.insert(ctr2+2,'factor')
                count -= 1
                let -= 1
        let += count2
        let += 1
        ## check if out of range
        if let >= len(more):
            return sente
        if  more[let] == '(':
            return factor()
        else:
            return 1
        
    elif more[let] == '(':
        return factor()
    else:
        return 1

def factor():
    global let
    sente.insert(len(sente)-1,"(")
    let += 1
    return expr()


def parsers(more):
    global let
    while let != len(more):
        if more[let] == '=' or let != 0:
            let += 1
            return assign()
        else:
            return 1

def devive(sente):            
    ctr3 = 0
    while ctr3 != len(token):
        if token[ctr3] == 'number' or token[ctr3] == 'id':
            token[ctr3] == 'id'
        ctr3 += 1
    ctr4 = 0
    while ctr4 != len(sente):
        if sente[ctr4] == 'expr' or sente[ctr4] == 'factor' or sente[ctr4] == 'term':         
            sente[ctr4] = 'id'
        ctr4 += 1
    ctr5 = 0
    while ctr5 != len(token) or ctr5 != len(sente):
        if token[ctr5] == sente[ctr5]:
            ctr5 += 1
        else:
            return False

    return True

#Main 1.0
counter1 = 0

while counter1 != int(counter):
    string = strings[counter1+1]
    if Tokenizer(str(string)) == 1:
        print("Line", counter1+1,end=': ')
        print(False)
    else:
        if parsers(moreToken(token)) == 1:
            print("Line", counter1+1,end=': ')
            print(False)
        else:
            print("Line",counter1+1,end=': ')
            print(devive(sente))
    #rewrite value
    token = []
    sente = []
    more = []
    ctr1 = 0
    let = 0
    ctr = 2
    counter1 += 1 

    
