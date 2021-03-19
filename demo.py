def sorting(File1):
  readfile = open(File1)
  names = []
  for line in readfile:
    temp = line.split()
    for i in temp:
      names.append(i)
  readfile.close()
  names.sort()
  with open("File2.txt", "w")as wf:

 
    
    for i in names:
        
        wf.write("Trainees of  march " + i + "batch : ")

        
        wf.write('\n')
        print (" TRAINEES OF" + i +  "MARCH BATCH : ")
        
        wf.writelines(" ")
   
  wf.close()
sorting("File1.txt")


     

 