count = 1
for i in range(1, 15,2):
    if count % 2 == 0:
        print((i*'O').center(15))
    else:
        print((i*'*').center(15))
    count += 1

       *       
      OOO      
     *****     
    OOOOOOO    
   *********   
  OOOOOOOOOOO  
 *************