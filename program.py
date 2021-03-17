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
        
        wf.write("Trainees of march batch : ")

        wf.write(i)
        wf.write('\n')
        print (" TRAINEES OF MARCH BATCH : ", i)
        
        wf.writelines(" ")
   
  wf.close()
sorting("File1.txt")


     