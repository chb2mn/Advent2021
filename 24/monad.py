from icecream import ic

w=0
x=0
y=0
z=0

def get_val(var):
    if var == 'w':
        return w
    elif var == 'x':
        return x
    elif var == 'y':
        return y
    elif var == 'z':
        return z
    else: 
        return int(var)
def set_val(var, the_inp):
    if var == 'w':
        global w
        w=the_inp
    elif var == 'x':
        global x
        x=the_inp
    elif var == 'y':
        global y
        y=the_inp
    elif var == 'z':
        global z
        z=the_inp

insts = []

with open('input.txt', 'r') as fin:
    for line in fin:
        line = line.strip()
        if line.startswith('inp'):
            insts.append([])
        insts[-1].append(line)

old_w = 0 
old_x = 0
old_y = 0
old_z = 0

C = [12,11,14,-6,15,12,-9,14,14,-5,-9,-5,-2,-7]
D = [4, 10,12,14,6,16,1,7,8,11,8,3,1, 8]

code = "41171183141291"
for i,inst in enumerate(insts):
    for line in inst:
        parts = line.split()
        if parts[0] == "inp":
            ic(i)
            set_val(parts[1], int(code[i]))    
        elif parts[0] == "add":
            if parts[2].startswith("-"):
                ic(x)
            set_val(parts[1], get_val(parts[1]) + get_val(parts[2]))
            if parts[2].startswith("-"):
                ic(x)
        elif parts[0] == "mul":
            set_val(parts[1], get_val(parts[1]) * get_val(parts[2]))
        elif parts[0] == "div":
            set_val(parts[1], get_val(parts[1]) // get_val(parts[2]))
            ic(z)
        elif parts[0] == "mod":
            set_val(parts[1], get_val(parts[1]) % get_val(parts[2]))
            ic(x)
        elif parts[0] == "eql":
            ic(get_val(parts[1]), get_val(parts[2]))
            set_val(parts[1], int(get_val(parts[1]) == get_val(parts[2])))
    ic(w,x,y,z)



