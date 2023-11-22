import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):

    with open(input_file_name,'r') as file, open (output_file_name,'w',newline='') as realpassfile:
        
        hash_dic={}
        for num in range(1000,10000):
            hashed_data=hashlib.sha256(str(num).encode('utf-8')).hexdigest()
            hash_dic[hashed_data]=num

        reader_file= csv.reader(file)   
        for row in reader_file:
            name= row[0]
            hashed_pas= row[1]
            for data in hash_dic.keys():
                if data == hashed_pas :
                    real_pas= hash_dic[data]
                    realpassfile.write(f"{name},{real_pas}\n")
    
    