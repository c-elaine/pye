largest_so_far = -1
print("Before", largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:
        largest_so_far = the_num

    print("After", largest_so_far)

zork = 0
print("Before", zork)

for thing in [9,41,12,3,74,15] :
    zork = zork + thing
    print(zork, thing)
print("After", zork)