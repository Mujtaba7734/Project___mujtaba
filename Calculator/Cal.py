operations,location = [],[]
equation_unmodified = input("plz enter equation without space ")
for x in range(len(equation_unmodified)):
    if not(equation_unmodified[x] >= "0" and equation_unmodified[x] <= "9"):
        operations.append(equation_unmodified[x])
        location.append(x) 
#notes down every operator and its location in the equation
#division
def division(equation): 
    Operator_No = 0
    while Operator_No < len(operations): 
        if operations[Operator_No] == "/":
            if Operator_No == 0:
                if  Operator_No == len(operations) -1:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1:]
                    value = float(nominator) / float(denominator)
                    equation = str(value)
                else:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1:location[Operator_No + 1]]
                    value = float(nominator) / float(denominator)
                    equation = str(value) + equation[location[Operator_No + 1]:]
                
            elif Operator_No == len(operations) - 1:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:]
                value = float(nominator) / float(denominator)
                equation = equation[:location[Operator_No - 1] + 1] + str(value)  
            else:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:location[Operator_No + 1]]
                value = float(nominator) / float(denominator)
                equation = equation[:location[Operator_No - 1] + 1] + str(value) + equation[location[Operator_No]+ 2:]
            operations.clear(),location.clear()
            for x in range(len(equation)):
                if not(equation[x] >= "0" and equation[x] <= "9"):
                    if equation[x] != ".":
                        operations.append(equation[x])
                        location.append(x)
        else: Operator_No +=1
    return equation
#multiplication
def multiplication(equation):
    Operator_No = 0
    while Operator_No < len(operations): 
        if operations[Operator_No] == "*":
            if Operator_No == 0:
                if  Operator_No == len(operations) - 1:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1: ]
                    value= float(nominator) * float(denominator)
                    equation = str(value)
                else:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1:location[Operator_No + 1]]
                    value= float(nominator) * float(denominator)
                    equation = str(value) + equation[location[Operator_No + 1]:]
                
            elif Operator_No == len(operations) - 1:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:]
                value= float(nominator) * float(denominator)
                equation = equation[:location[Operator_No - 1] + 1] + str(value) 
            else:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:location[Operator_No + 1]]
                value= float(nominator) * float(denominator)
                equation = equation[:location[Operator_No - 1] + 1] + str(value) + equation[location[Operator_No]+ 2:]
            operations.clear(),location.clear()
            for x in range(len(equation)):
                if not(equation[x] >= "0" and equation[x] <= "9"):
                    if equation[x] != ".":
                        operations.append(equation[x])
                        location.append(x)
        else: Operator_No += 1
    return equation
#addition
def addition(equation):
    Operator_No = 0
    while Operator_No < len(operations): 
        if operations[Operator_No] == "+":
            if Operator_No == 0:
                if  Operator_No == len(operations) -1:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1: ]
                    value= float(nominator) + float(denominator)
                    equation = str(value)
                else:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 1: location[Operator_No + 1]]
                    value= float(nominator) + float(denominator)
                    equation = str(value) + equation[location[Operator_No + 1]:]
                
            elif Operator_No == len(operations) - 1:
                nominator = equation[location[Operator_No - 1]+1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:]
                if operations[Operator_No -1] == "-":
                    nominator = equation[location[Operator_No - 1]:location[Operator_No]] 
                value= float(nominator) + float(denominator)  
                if value > 0:
                    equation = equation[:location[Operator_No - 1]] + "+" +str(value)
                    Operator_No = 0
                else:equation = equation[:location[Operator_No - 1]+ 1] + str(value) 
            else:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 1:location[Operator_No + 1]]
                if operations[Operator_No -1] == "-":
                    nominator = equation[location[Operator_No - 1]:location[Operator_No]] 
                value= float(nominator) + float(denominator)
                if value > 0:
                    equation = equation[:location[Operator_No - 1]] + "+" +str(value)
                    Operator_No = 0
                else:equation = equation[:location[Operator_No - 1]+ 1] + str(value) 
                equation = equation[:location[Operator_No - 1] + 1] + str(value) + equation[location[Operator_No]+ 2:]
            operations.clear(),location.clear()
            for x in range(len(equation)):
                if not(equation[x] >= "0" and equation[x] <= "9"):
                    if equation[x] != ".":
                        operations.append(equation[x])
                        location.append(x)
        else: Operator_No +=1
    return equation
#subtraction
def subtraction(equation):
    Operator_No = 0
    while Operator_No < len(operations): 
        if operations[Operator_No] == "-" :
            if location[Operator_No] != 0:
                if Operator_No == 0:
                    if  Operator_No == len(operations) - 1:
                        nominator =equation[:location[Operator_No]]
                        denominator = equation[location[Operator_No] + 1:]
                        value= float(nominator) - float(denominator)
                        equation = str(value)
                    else:
                        nominator =equation[:location[Operator_No]]
                        denominator = equation[location[Operator_No] + 1:location[Operator_No + 1]]
                        value= float(nominator) - float(denominator)
                        equation = str(value) + equation[location[Operator_No + 1]:]
                    
                elif Operator_No == len(operations) - 1:
                    nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                    denominator = equation[location[Operator_No]+ 1:]
                    value= float(nominator) - float(denominator)
                    equation = equation[:location[Operator_No - 1] + 1] + str(value) 
                else:
                    nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                    denominator = equation[location[Operator_No]+ 1:location[Operator_No + 1]]
                    value= float(nominator) - float(denominator)
                    equation = equation[:location[Operator_No - 1] + 1] + str(value) + equation[location[Operator_No]+ 2:]
                operations.clear(),location.clear()
                for x in range(len(equation)):
                    if not(equation[x] >= "0" and equation[x] <= "9"):
                        operations.append(equation[x])
                        location.append(x)
            else:
                if Operator_No == 0 and len(operations) != 1:
                    if  Operator_No == len(operations) - 2:
                        nominator =equation[:location[Operator_No + 1]]
                        denominator = equation[location[Operator_No +1] + 1:]
                        value= float(nominator) - float(denominator)
                        equation = str(value)
                    else:
                        nominator =equation[:location[Operator_No +1]]
                        denominator = equation[location[Operator_No + 1] + 1:location[Operator_No + 2]]
                        value= float(nominator) - float(denominator)
                        equation = str(value) + equation[location[Operator_No + 2]:]
                operations.clear(),location.clear()   
                for x in range(len(equation)):
                        if not(equation[x] >= "0" and equation[x] <= "9"):
                            if equation[x] != ".":
                                operations.append(equation[x])
                                location.append(x)
                if operations[0] == "-" and len(operations) == 1:
                    Operator_No +=1
        else: Operator_No +=1
    return(equation) 
#exponent(power)
def exponent(equation):
    Operator_No = 0
    while Operator_No < len(operations) and len(operations) - Operator_No!= 1 : 
        concurrent = location[Operator_No + 1] - location[Operator_No] 
        if operations[Operator_No] == "*" and operations[Operator_No +1] == "*" and concurrent == 1:
            if Operator_No == 0:
                if  Operator_No == len(operations) -2:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No] + 2:]
                    value = int(int(nominator) ** int(denominator))
                    equation = str(value)
                else:
                    nominator =equation[:location[Operator_No]]
                    denominator = equation[location[Operator_No + 1] + 1:location[Operator_No + 2]]
                    value = int(int(nominator) ** int(denominator))
                    equation = str(value) + equation[location[Operator_No + 2]:]
                
            elif Operator_No == len(operations) - 2:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No]+ 2:]
                value = int(int(nominator) ** int(denominator))
                equation = equation[:location[Operator_No - 1] + 1] + str(value)  
            else:
                nominator = equation[location[Operator_No - 1]+ 1:location[Operator_No]]
                denominator = equation[location[Operator_No +1]+ 1:location[Operator_No + 2]]
                value = int(int(nominator) ** int(denominator))
                equation = equation[:location[Operator_No - 1] + 1] + str(value) + equation[location[Operator_No + 1]+ 2:]
            operations.clear(),location.clear()
            for x in range(len(equation)):
                if not(equation[x] >= "0" and equation[x] <= "9"):
                    operations.append(equation[x])
                    location.append(x)
        else: Operator_No +=1
    return equation
brackets_open = []
brackets_close = []
for x in range(len(operations)): #checks whether data entered contains a bracket or not
    if operations[x] == "(":
        brackets_open.append(location[x])
    if operations[x] == ")":
        brackets_close.append(location[x])
if len(brackets_close) != 0 and len(brackets_close) != 0: 
    equation_brackets = equation_unmodified[brackets_open[0] +1:brackets_close[0]]
    operations.clear(),location.clear()
    for x in range(len(equation_brackets)):
        if not(equation_brackets[x] >= "0" and equation_brackets[x] <= "9"):
            operations.append(equation_brackets[x])
            location.append(x)
    equation_brackets = exponent(equation_brackets) #solves data in brackets
    equation_brackets = division(equation_brackets)
    equation_brackets = multiplication(equation_brackets)
    equation_brackets = addition(equation_brackets)
    equation_brackets = subtraction(equation_brackets)
    operations.clear(),location.clear()
    for x in range(len(equation_unmodified)): 
        if not(equation_unmodified[x] >= "0" and equation_unmodified[x] <= "9"):
            operations.append(equation_unmodified[x])
            location.append(x)
            if equation_unmodified[x] != ".":
                operations.append(equation_unmodified[x])
                location.append(x)
    if brackets_open[0] == 0: #adds solved brackets data and concatinates into orignal equation
        if brackets_close[0] == len(equation_unmodified) - 1:
            equation_final =equation_brackets
            equation_unmodified = None
        else:
            equation_unmodified = equation_brackets + equation_unmodified[brackets_close[0]+1:]
    elif brackets_close[0] ==len(equation_unmodified) -1:
        equation_unmodified = equation_unmodified[:brackets_open[0]] + equation_brackets
    else: 
        equation_unmodified = equation_unmodified[:brackets_open[0]] + equation_brackets + equation_unmodified[brackets_close[0] + 1:]     


if equation_unmodified is not None: #solves the final equation according to BODMAS principal to give final results
    operations.clear(),location.clear()
    for x in range(len(equation_unmodified)):
        if not(equation_unmodified[x] >= "0" and equation_unmodified[x] <= "9"):
            if equation_unmodified[x] != ".":
                operations.append(equation_unmodified[x])
                location.append(x)      
    equation_unmodified = exponent(equation_unmodified)
    equation_unmodified = division(equation_unmodified)
    equation_unmodified = multiplication(equation_unmodified)
    equation_unmodified = addition(equation_unmodified)
    equation_unmodified = subtraction(equation_unmodified)
    equation_final = equation_unmodified
print(equation_final)
