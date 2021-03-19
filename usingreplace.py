def trainee_name():

    with open ("read.txt","r")as rf:
        lines_to_read=[2]
        for position,line in enumerate(rf):
            if position in lines_to_read:
                str = "Trainee name of march batch   "
                x = str.replace("name","ram")
                
                            
                print(x)

                try:
                
                    with open ("write.txt","w")as wf:

                        wf.write(x)
                       
                except ValueError:
                    print("The name is not in the content")        
                finally:
                    wf.close()
trainee_name()              

   







 