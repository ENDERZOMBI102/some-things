#brainfuck interpreter
values = [0]
pointer = 0
print("Welcome to EZ102's brainfuck interpreter!\nyou can insert here the name of the file!\n(filename no extension(.ebf))")
prg = input()# get the input

with open("./"+prg+".ebf", "r") as file:#open the file
    prg = file.read()#read the file

prg = list(prg.split(" "))#trasform the string to a list
for cmd in prg:#for every code char
    if cmd == ">":#increment the pointer
        pointer += 1
        if len(values) < pointer:
            values.append(0)
    elif cmd == "<":#decrement the pointer
        pointer -=  1
        if pointer == -1:
            pointer = len(values)
    elif cmd == "+":#increment the pointed value
        values[pointer]+=1
    elif cmd == "-":#decrement the pointed value
        values[pointer]-=1
    elif cmd == ".":#output the charater
        print(chr(values[pointer]), end="")
    elif cmd == ",":#input a character
        values[pointer] = ord(input())
print("end interpretation.")