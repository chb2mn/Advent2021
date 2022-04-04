from icecream import ic

_left_slot = [None,None]
_right_slot = [None,None]
_ab_slot = None
_bc_slot = None
_cd_slot = None
_a_room=["D","B"]
_b_room=["D","C"]
_c_room=["B","A"]
_d_room=["A","C"]

max_score = 16244

def move_a(spaces):
    return spaces
def move_b(spaces):
    return 10*spaces
def move_c(spaces):
    return 100*spaces
def move_d(spaces):
    return 1000*spaces

calc_score = 0

#A to left slot
calc_score += move_a(9)
calc_score += move_a(9)
#Cc to right slot
calc_score += move_c(5)
calc_score += move_c(5)
#D to d room x4
calc_score += move_d(9)
calc_score += move_d(10)
calc_score += move_d(10)
calc_score += move_d(10)
#b to cd slot
calc_score += move_b(9)
#a to a room x2
calc_score += move_a(5)
calc_score += move_a(5)
#b to left slot x2
calc_score += move_b(7)
calc_score += move_b(7)
#a to a room x2
calc_score += move_a(9)
calc_score += move_a(9)
#c to c room
calc_score += move_c(8)
#b to ab slot
calc_score += move_b(4)
#c to c room
calc_score += move_c(9)
#b to b room
calc_score += move_b(5)
#b to b room x2
calc_score += move_b(6)
calc_score += move_b(6)
#b to b room
calc_score += move_b(4)
#c to c room x2
calc_score += move_c(5)
calc_score += move_c(5)
ic(calc_score)




