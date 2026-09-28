members = []
print("Rejister Part")
while True :
    new_mem = input("Input name to register ('end' for end)")
    if new_mem == 'end' :
        break
        
    elif new_mem in members :
        print(f"{new_mem}is duplicated.")
    else :
        members.append(new_mem)
print(members)
