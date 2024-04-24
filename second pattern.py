def print_pattern_E(height):
    width = height-2
    
    for i in range(height):
        if i==0 or i==height//2 or i==height-1:
            print("*"*(width+2))
        else:
            print("*")
            
height=int(input("Enetr the height of the letter E: "))
print_pattern_E(height)