#eric
print a square of user inputsquare_height = int(input("How high is the square?"))square_wide = int(input("How wide is the square?"))a = 1b = 1while b <= square_height:    if b == 1 or b == square_height:        while a <= square_wide:            print("*", end='')            a += 1    else :        a = 2        print("*", end='')        while a <= square_wide - 1:            print(" ", end='')            a += 1        print("*", end='')    print()    a = 1    b +=1
#Katy
def square():
    i=1
    while i <=5:
        print("*****")
        i += 1
square()

def square2():
    i=1
    user_input = int(input("How big is the square? "))
    while i <= user_input:
        print("*" * user_input)
        i += 1
square2()

# board = []
# # for x in range(1, 5):
# #   board.append(["O"] * 5)
# # def print_board(board):
# #   for row in board:
# #     print " ".join(row)
# # print_board(board)