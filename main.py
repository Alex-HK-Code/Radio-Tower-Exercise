def display(l):
    layer = ""
    for i in range(20):
        if(l[i] == 1):
            layer += "|"
        else:
            layer += "-"
    for i in range(3):
        print(layer)

def build(l,ind):
    l[ind-1] = 1
    return l 



towers = [0] * 20
while(True):
    user_input = input("Enter '0' to exit | Enter '1' to display the radio towers | Enter '2' to build a radio tower\n")
    if(user_input == str(0)):
        break 

    elif(user_input == str(1)):
        display(towers)

    elif(user_input == str(2)):
        tower_location = input("between 1-20, choose a location to build the tower\n")
        towers = build(towers, int(tower_location))

