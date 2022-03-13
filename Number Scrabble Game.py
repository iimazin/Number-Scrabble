numbers = [1,2,3,4,5,6,7,8,9]
player1_numbers = []
player2_numbers = []

def update_lists(n, li):
    li.append(n)
    numbers.remove(n)

def take_input(player_name, player_nums):
    input_message = player_name + " plays, take a number: "
    num = int(input(input_message))

    if num in numbers:
        update_lists(num, player_nums)
    else:
        take_input(player_name, player_nums)


while len(numbers) > 1:
    print (numbers)
    take_input("player 1", player1_numbers)
    take_input("player 2", player2_numbers)
    print("-------")
    if len(numbers) > 3:
            print (numbers)
            take_input("player 1", player1_numbers)
            take_input("player 2", player2_numbers)
            print("-------")
    else:
        print (numbers)
        take_input("player 1", player1_numbers)
        take_input("player 2", player2_numbers)
        print("-------")
        if player1_numbers [0] + player1_numbers [1] + player1_numbers [2] == 15:
            print ("Player 1 wins!")
            break
        elif player1_numbers [0] + player1_numbers [1] + player1_numbers [3] == 15:
            print ("Player 1 wins!")
            break
        elif player1_numbers [1] + player1_numbers [2] + player1_numbers [3] == 15:
                print ("Player 1 wins!")
                break
        elif player1_numbers [0] + player1_numbers [2] + player1_numbers [3] == 15:
                print ("Player 1 wins!")
                break
        elif player2_numbers [0] + player2_numbers [1] + player2_numbers [2] == 15:
                print ("Player 2 wins!")
                break
        elif player2_numbers [0] + player2_numbers [1] + player2_numbers [3] == 15:
                print ("Player 2 wins!")
                break
        elif player2_numbers [1] + player2_numbers [2] + player2_numbers [3] == 15:
                print ("Player 2 wins!")
                break
        elif player2_numbers [0] + player2_numbers [2] + player2_numbers [3] == 15:
                print ("Player 2 wins!")
                break
        else:
                print("Draw")
                break