my2dlist=[[2,5,8],[3,7,4],[1.6,9],[4,2,0]]
userrow=int(input('what row do you want displayed'))
print(*my2dlist[userrow])
usercolumn=int(input('which column in this row do you want displayed'))
print(my2dlist[userrow][usercolumn])
userchoice=input('do you want to chage that value').upper

# Github is working with my new laptop
if userchoice=="Yes":
    replacement=int(input('what do you want to replace it with'))
    my2dlist[userrow][usercolumn]=replacement
    print(my2dlist[userrow][usercolumn]) 
    
