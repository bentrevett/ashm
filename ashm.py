reg = {"R"+str(x):0 for x in range(16)}
labels = dict()

def execute(code, pc):
    
    print("parsing code into instructions...")
    
    split_code = code.split('\n')
    
    print("parsing labels...")
    
    for c in range(len(split_code)):
        if split_code[c].split(' ')[0] == 'LBL':
            labels[split_code[c].split(' ')[1]] = c
            
    print("begin execution loop...")
    
    while pc < len(split_code)-1:
    
        instruction = split_code[pc]
        
        tokens = tokenize(instruction)
        
        #tokens[0] = operation
        #tokens[1] = operand 1
        #tokens[2] = operand 2
        #tokens[3] = operand 3, etc.
        
        if tokens[0] == 'MOV':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] = reg[tokens[2]]
            else:
                reg[tokens[1]] = int(tokens[2])
            pc += 1
        
        elif tokens[0] == 'ADD':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] += reg[tokens[2]]
            else:
                reg[tokens[1]] += int(tokens[2])
            pc += 1
            
        elif tokens[0] == 'SUB':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] -= reg[tokens[2]]
            else:
                reg[tokens[1]] -= int(tokens[2])
            pc += 1
            
        elif tokens[0] == 'MUL':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] *= reg[tokens[2]]
            else:
                reg[tokens[1]] *= int(tokens[2])
            pc += 1
            
        elif tokens[0] == 'DIV':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] = reg[tokens[1]] // reg[tokens[2]]
            else:
                reg[tokens[1]] = reg[tokens[1]] // int(tokens[2])
            pc += 1
        
        elif tokens[0] == 'MOD':
            print(tokens[0])
            if tokens[2][0] == 'R':
                reg[tokens[1]] = reg[tokens[1]] % reg[tokens[2]]
            else:
                reg[tokens[1]] = reg[tokens[1]] % int(tokens[2])
            pc += 1
        
        elif tokens[0] == 'LBL':
            print(tokens[0])
            pc += 1
            
        elif tokens[0] == 'JEQ':
            print(tokens[0])
            if reg[tokens[1]] == reg[tokens[2]]:
                pc = labels[tokens[3]]
            else:
                pc += 1
                
        elif tokens[0] == 'JGT':
            print(tokens[0])
            if reg[tokens[1]] > reg[tokens[2]]:
                pc = labels[tokens[3]]
            else:
                pc += 1
                
        elif tokens[0] == 'JLT':
            print(tokens[0])
            if reg[tokens[1]] < reg[tokens[2]]:
                pc = labels[tokens[3]]
            else:
                pc += 1
              
        elif tokens[0] == 'JGZ':
            print(tokens[0])
            if reg[tokens[1]] > 0:
                pc = labels[tokens[2]]
            else:
                pc += 1
            
        elif tokens[0] == 'JLZ':
            print(tokens[0])
            if reg[tokens[1]] < 0:
                pc = labels[tokens[2]]  
            else:
                pc += 1
                
        elif tokens[0] == 'JEZ':
            print(tokens[0])
            if reg[tokens[1]] == 0:
                pc = labels[tokens[2]]  
            else:
                pc += 1

        else:
            print("UNDEFINED OPERAND")
            exit()
            
    display(reg)
        

def display(dic):
    for i in range(16):
        print("R"+str(i)+":"+str(dic["R"+str(i)]),end=' ')
    print("\n")
    
def tokenize(code):
    return code.strip('\n').split(' ')

def main():

    pc = 0

    print("opening file...")

    f = open("ashm.txt", 'r')

    print("reading file...")

    code = f.read()
    
    execute(code, pc)
    
if __name__ == "__main__": 
    main()
