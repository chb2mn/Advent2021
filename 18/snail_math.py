from icecream import ic
import json
import re
'''
def split(l):
    if isinstance(l[0],int):
        if l[0] > 9:
            l[0] = [l[0]//2, (l[0]+1)//2]
    else:
        split(l[0])
    if isinstance(l[1],int):
        if l[1] > 9:
            l[1] = [l[1]//2, (l[1]+1)//2]
    else:
        split(l[1])
'''

big_int_re = re.compile(r'(\d\d+)')
def cheese_split(l):
    l = str(l)
    val = int(big_int_re.search(l).group(0))
    new_val = f"[{val//2},{(val+1)//2}]"

    l = big_int_re.sub(new_val, l, count=1)
    return json.loads(l)

#l=[0,11]
#l=cheese_split(l)
#ic(l)
#l = [[[12,0],1],2]
#l=cheese_split(l)
#ic(l)
#ic(cheese_split([[2,13],3]))

def magnitude(l):
    my_sum = 0
    if isinstance(l, int):
        return l
    else:
        return 3*magnitude(l[0])+2*magnitude(l[1])

#
#ic(magnitude([[1,2],[[3,4],5]]))
#ic(magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))

int_re = re.compile(r'\d+')
#ic("".join(reversed(str(int_re.sub(str(3+4), "".join(reversed("[3,2,3]")), count=1)))))

def back_replace(s, i):
    try:
        val = int_re.search("".join(reversed(s))).group(0)
        val = "".join(reversed(val))
        val = str(int(val) + i)
        val = "".join(reversed(val))
        return "".join(reversed(str(int_re.sub(val, "".join(reversed(s)), count=1))))
    except AttributeError:
        return s
   
def cheese_explode(l):
    stack = []
    old_str = str(l).replace(' ','')
    new_str = ''
    popping = False
    hit = False
    j= ''
    k= ''
    far_right = ''
    for i, c in enumerate(old_str):
        if hit:
            new_str+=c
            continue
        if popping:
            if c == ']':
                stack.pop()
                k = int(k)
                new_str+='0'
                popping = False
                j = ''
                continue
            try:
                if c == ',':
                    j = int(j)
                    new_str = back_replace(new_str, j)
                    continue
                if isinstance(j, str):
                    j += c
                elif isinstance(j, int) and isinstance(k, str):
                    k+=c
                continue
            except ValueError:
                continue
        if c == '[':
            stack.append(c)
            if len(stack) > 4 and isinstance(k, str):
                popping = True
                continue
        elif c == ']':
            stack.pop()
        if isinstance(k, int):
            if c.isnumeric():
                far_right += c
            elif not c.isnumeric() and len(far_right)>0:
                new_str += str(int(far_right) + k)
                new_str += c
                k = ''
                hit=True
            else:
                new_str += c
                continue
        else:
            new_str += c
    #try:
    return json.loads(new_str)
    #except:
    #    ic(new_str)
    #    quit()

#l = [[[[[9,8],1],2],3],4]
#l = cheese_explode(l)
#ic(l)
#l = [7,[6,[5,[4,[3,2]]]]]
#l = cheese_explode(l)
#ic(l)
#l = [[6,[5,[4,[3,2]]]],1]
#l = cheese_explode(l)
#ic(l)
#l = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
#l = cheese_explode(l)
#ic(l)
#l = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
#l = cheese_explode(l)
#ic(l)
#l = [[[[[1,1],1],[[1,1],1],1],1],1]
#l = cheese_explode(l)
#ic(l)
#l=[[[[3,3],[[1,1],[2,2]]],[4,4]],[5,5]]
#l = cheese_explode(l)
#ic(l)
#l = cheese_explode(l)
#ic(l)
#quit()

def check_reduced(l, i =0):
    '''
    0=reduced
    2=explode
    1=split
    '''
    if i>4:
        return 2
    elif isinstance(l, int):
        if l>9:
            return 1
        return 0
    else:
        return max(check_reduced(l[0], i+1), check_reduced(l[1], i+1))


data = []
with open('input.txt', 'r') as fin:
    for line in fin:
        data.append(json.loads(line))

#data = [[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]]
#data = [
#        [1,1],
#        [2,2],
#        [3,3],
#        [4,4],
#        [5,5],
#        [6,6]
#]
#data = [
#        [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
#        [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
#        [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
#        [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
#        [7,[5,[[3,8],[1,4]]]],
#        [[2,[2,2]],[8,[8,1]]],
#        [2,9],
#        [1,[[[9,3],9],[[9,0],[0,7]]]],
#        [[[5,[7,4]],7],1],
#        [[[[4,2],2],6],[8,7]]
#]
ans = None

part =2
if part ==1:
    for line in data:
        if ans is None:
            ans = line
            uh=False
        else:
            ans = [ans, line]
            uh=True
        q = check_reduced(ans)
        while q:
            if q == 2:
                ans=cheese_explode(ans)
            elif q == 1:
                ans=cheese_split(ans)
            q = check_reduced(ans)
        ic(ans)    
        ic(magnitude(ans))

else:
    max_mag = 0
    for line in data:
        for line2 in data:
            if line !=line2:
                ans=[line,line2]
                q = check_reduced(ans)
                while q:
                    if q == 2:
                        ans=cheese_explode(ans)
                    elif q == 1:
                        ans=cheese_split(ans)
                    q = check_reduced(ans)
                ic(ans)    
                ic(magnitude(ans))
                max_mag=max(max_mag, magnitude(ans))
    ic(max_mag)
