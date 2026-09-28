import random
num = random.randint(1,10)
round = 0
lose = False
print(f"-->{num}")
while round < 3 and not lose :
    ans = str(input(f"[{round+1}] Next number more(m) or less(l) than-->{num}:  "))
    newnum = random.randint(1,10)
    print(f"-->{newnum}")
    if newnum == num :
        round += 1
    elif ans == 'm' and newnum > num :
        round += 1
    elif ans == 'l' and newnum < num :
        round += 1
    else :
        lose = True
    num = newnum
if round == 3 and not lose :
    print(f"Correct {round} turn -->YouWin (^ ^)")
else :
    print(f"Correct {round} turn -->YouLose (T T)")