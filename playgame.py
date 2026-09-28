members = []
def regist():
    while True :
        new_mem = input("Input name to register ('end' for end): ")
        if new_mem == 'end' :
            break
        elif new_mem in members :
            print(f"{new_mem}is duplicated.")
        else :
            members.append(new_mem)
    print(f"All members is {members}")
def menu_game() :
    while True :
        print(f"Hello {player}")
        print("1.Guess Number")
        print("2.More or Less")
        ans = int(input("Select Game or 0 to exit :"))
        if ans == 0 :
            break
        elif ans == 1 :
            print("Play Guess")
            import guess
        elif ans == 2 :
            print("Play More or Less")
            import ml
play = True
while play :
    player = input("Player name ('exit' to exit): ")
    if player in members :
        print("Play game")
        menu_game()
    elif player == 'exit' :
        play = False        
    else :
        print("Rejister Part")
        regist()
print("Thank you for play")
