import os
import csv 
import random

Names=[]

def Fill_Csv():
    fields = ['ID', 'Name'] 
    filename = "data.csv"
    Names.pop(0)
    rows=[]
    id=0
    for name in Names:
        id+=1
        rows.append([id,name])
        #print(rows)
    with open(filename, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)

    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

def Rename_Files():
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    training_folder=os.path.join(BASE_DIR,"Images\Training")

    for root,dirs,files in os.walk(training_folder):
        Names.append(os.path.basename(os.path.normpath(root))) 
        print("Names: {}".format(Names))
        tmp_counter=0
        current_folder=(os.path.basename(os.path.normpath(root))).replace(" ","_")
        cwd=root
        for img in files:
            old_name=os.path.join(cwd,img)
            random_name=random.randrange(0, 999)
            new_name=os.path.join(cwd,current_folder+str(random_name+tmp_counter)+".jpg")
            print("old:{}".format(old_name))
            print("new:{}".format(new_name))
            if not os.path.exists(new_name):
                os.rename(old_name,new_name)
            tmp_counter+=1
Rename_Files() 
Fill_Csv()