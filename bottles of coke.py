#2017/09
bottles = 99;
bottles1 = 98;
while bottles > 1:
    print (str(bottles)+" bottles of coke on the wall, " + str(bottles) +' bottles of coke.')
    
    print ('Take one down down and pass it around ' + str(bottles1)+' of coke on the wall.')

    print(' ')
    
    

    bottles-=1
    bottles1-=1

if (bottles == 1):
    print ('1 bottle of coke on the wall, 1 bottle of coke.')
    print ("Take on down pass it around, no more bottles of coke on the wall.")
    print (" ")
    print ("No more bottles of coke on the wall, no more bottles of coke.")
    print ("Go to the store buy some more, 99 bottles of coke on the wall.")
