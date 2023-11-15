operations,location = [],[]
equation_unmodified = input("plz enter equation without space ")
for x in range(len(equation_unmodified)):
    if not(equation_unmodified[x] >= "0" and equation_unmodified[x] <= "9"):
        operations.append(equation_unmodified[x])
        location.append(x)
     
#notes down every operator and its location in the equation
#division
def operations_update(equation):
    global operations, location
    operations.clear(),location.clear()   
    for x in range(len(equation)):
            if not(equation[x] >= "0" and equation[x] <= "9"):
                if equation[x] != ".":
                    operations.append(equation[x])
                    location.append(x)
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
                        if equation[x] != ".":
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
                    if equation[x] != ".":
                        operations.append(equation[x])
                        location.append(x)
        else: Operator_No +=1
    return equation
def equation_solver(equation):
    equation  = exponent(equation)
    equation = division(equation)
    equation = multiplication(equation)
    equation = addition(equation)
    equation = subtraction(equation)
    return equation
bracket_open = []
bracket_close = []
def brackets_update(equation):
    global operations, location
    bracket_open.clear(), bracket_close.clear()
    for x in range(len(equation)):
            if equation[x] == "(":
                bracket_open.append(x)
            elif equation[x] == ")":
                bracket_close.append(x)
brackets_update(equation_unmodified)
index = 0
while len(bracket_open) != 0:
    if len(bracket_open) == 1:
        equation_bracket =equation_unmodified[bracket_open[index] + 1:bracket_close[index]]
        operations_update(equation_bracket)
        equation_bracket = equation_solver(equation_bracket)
        if equation_bracket[0] == "-":
            equation_bracket = equation_bracket[1:]
            if equation_unmodified[bracket_open[index] - 1] == equation_bracket[0]:
                equation_unmodified = equation_unmodified[:bracket_open[index] - 1] + "+" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
            else:
                equation_unmodified = equation_unmodified[:bracket_open[index] - 1] + "-" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
        else:
            equation_unmodified = equation_unmodified[:bracket_open[index]] + equation_bracket + equation_unmodified[bracket_close[index] + 1:]    
        bracket_open.pop(index)
    elif bracket_open[index + 1] < bracket_close[index]:
        equation_bracket = equation_unmodified[bracket_open[index + 1]+ 1:bracket_close[index]]
        operations_update(equation_bracket)
        equation_bracket = equation_solver(equation_bracket)
        if equation_bracket[0] == "-":
            equation_bracket = equation_bracket[1:]
            if equation_unmodified[bracket_open[index + 1] - 1] == equation_bracket[0]:
                equation_unmodified = equation_unmodified[:bracket_open[index + 1] - 1] + "+" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
            else:
                equation_unmodified = equation_unmodified[:bracket_open[index + 1] - 1] + "-" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
        else:
            equation_unmodified = equation_unmodified[:bracket_open[index + 1]] + equation_bracket + equation_unmodified[bracket_close[index] + 1:]    
        brackets_update(equation_unmodified)
    else:
        equation_bracket =equation_unmodified[bracket_open[index] + 1:bracket_close[index]]
        operations_update(equation_bracket)
        equation_bracket = equation_solver(equation_bracket)
        if equation_bracket[0] == "-":
            equation_bracket = equation_bracket[1:]
            if equation_unmodified[bracket_open[index] - 1] == equation_bracket[0]:
                equation_unmodified = equation_unmodified[:bracket_open[index] - 1] + "+" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
            else:
                equation_unmodified = equation_unmodified[:bracket_open[index] - 1] + "-" + equation_bracket + equation_unmodified[bracket_close[index] + 1:]
        else:
            equation_unmodified = equation_unmodified[:bracket_open[index]] + equation_bracket + equation_unmodified[bracket_close[index] + 1:]    
        brackets_update(equation_unmodified)
if equation_unmodified is not None: #solves the final equation according to BODMAS principal to give final results
    operations_update(equation_unmodified)
    equation_final = equation_solver(equation_unmodified)
print(equation_final)
#20*40-10+50-(20-30)+(100-90)
#2**(-1-1)
#2**(-2)