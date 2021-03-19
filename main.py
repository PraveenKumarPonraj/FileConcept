import csv

with open('Readcsv.txt', 'r') as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    
    
    for row in csv_reader:

        with open('writecsv.txt', 'w') as wf:
            
            
            wf.write(f' my name is  { row["name"]} ,i am  {row["age"]} years old .')
      
   

    