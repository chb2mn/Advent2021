from pprint import pprint

class Bingo():
    def __init__(self, board):
        self.board = board
        self.marked_board=[[False for i in range(len(board[0]))] for i in range(len(board))]
    
    def mark(self,called_num):
        for i, row in enumerate(self.board):
            for j, num in enumerate(row): 
                if called_num == num:
                    self.marked_board[i][j] = True

    def check_win(self):
        if any([all(row) for row in self.marked_board]):
            return True #checked
        if any([all(row[i] for row in self.marked_board) for i in range(len(self.marked_board))]):
            return True #checked
        '''
        if all([self.marked_board[i][i] for i in range(len(self.marked_board))]):
            return True #checked
        if all(self.marked_board[i][len(self.marked_board)-1-i] for i in range(len(self.marked_board))):
            return True #checked
        '''
        return False

    def get_score(self):
        my_sum = 0
        for i, row in enumerate(self.marked_board):
            for j, is_marked in enumerate(row):
                if not is_marked:
                    my_sum += int(self.board[i][j])
        return my_sum
#debug code

bingo = Bingo([[1,2,3],[4,5,6],[7,8,9]])
bingo.mark(3)
print(bingo.check_win())
bingo.mark(5)
print(bingo.check_win())
bingo.mark(7)
print(bingo.marked_board)
print(bingo.check_win())

part = 2
called_nums = []
boards = []
with open('input.txt', 'r') as fin:
    called_nums = fin.readline().split(',')
    current_board =[]
    for line in fin:
        line=line.strip()
        if line == '':
            if len(current_board) > 0:
                boards.append(Bingo(current_board))
            current_board=[]
        else:
            row = line.split()
            current_board.append(row)
if part ==1:
    for num in called_nums:
        for board in boards:
            board.mark(num)
            if (board.check_win()):
                pprint(board.board)
                pprint(board.marked_board)
                print("Last Number:", num)
                print("Winner:", board.get_score())
                print("x*y:", int(num)*board.get_score())
        if (any(board.check_win() for board in boards)):
            #pprint([board.marked_board for board in boards])
            break
if part ==2:
    for num in called_nums:
        to_delete = []
        for i, board in enumerate(boards):
            board.mark(num)
            if board.check_win():
                to_delete.append(i)
        if len(boards)>1:
            for i in reversed(to_delete):
                boards.pop(i)
        else:
            if (board.check_win()):
                print("Last Number:", num)
                print("Winner:", board.get_score())
                print("x*y:", int(num)*board.get_score())
                break
