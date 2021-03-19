def trainee_name():

    with open ("read.txt","r")as rf:
        lines_to_read=[8]
        for position,line in enumerate(rf):
            if position in lines_to_read:
                str = "Trainee %s of march batch  "
                name = line
                print(str % name)
                


                try:
                    with open ("write.txt","w")as wf:

                        wf.write("Trainee %s of march batch  "% name)


                except ValueError:
                    print("The name is not in the content")        
                finally:
                    wf.close()
                    
trainee_name()              

   







 