# from PIL import Image

# im = Image.open("bridge.png")
# im.rotate(45).show()

# mak= open('mak.txt')
# print(type(mak.readlines()))
# print(type(mak.read()))
# print(type(mak.readline()))

import csv
from statistics import mean 
#1
with open('grade.csv','r') as file , open('output1.csv','w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg= mean(grade_list)
            final_list.append([name,avg])    
        writer = csv.writer(out)
        writer.writerows(final_list)

#2
with open('grade.csv','r') as file , open('output2.csv','w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[int(grade) for grade in row[1:]]
            avg=mean(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(item[1],item[0]))}
        # sorted_avg= dict(sorted(dic.items(), key=lambda item:item[1]))
        writer = csv.writer(out)
        for row in sorted_avg.items():
            writer.writerow(row)

#3
with open('grade.csv','r') as file , open('output3.csv','w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg=sum(grade_list)/len(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(-item[1],item[0]))}
        top3=dict(list(sorted_avg.items())[:3])
        writer = csv.writer(out)
        for row in top3.items():
            writer.writerow(row)


#4
# with open('grade.csv','r') as file , open('output1.csv','w', newline='') as out:
#         reader= csv.reader(file)
#         final_list=[]
#         dic={}
#         for row in reader:
#             name=row[0]
#             grade_list=[int(grade) for grade in row[1:]]
#             avg=sum(grade_list)/len(grade_list)
#             final_list.append([name,avg])  
#             dic[name] =avg
#         sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(item[1],item[0]))}
#         floor3=list(sorted_avg.values())[:3]
#         print(floor3)
#         writer = csv.writer(out)
#         for item in floor3:
#             writer.writerow([item])

#5
# with open('grade.csv','r') as file , open('output1.csv','w', newline='') as out:
#         reader= csv.reader(file)
#         final_list=[]
#         dic={}
#         for row in reader:
#             name=row[0]
#             grade_list=[int(grade) for grade in row[1:]]
#             avg=sum(grade_list)/len(grade_list)
#             final_list.append([name,avg])  
#             dic[name] =avg
#         list_avg= list(dic.values())
#         avg_avg= [sum(list_avg)/ len(list_avg)]
#         print(avg_avg)
#         writer = csv.writer(out)
#         for item in avg_avg:
#             writer.writerow([item])
       
       
       
# with open('hashed_pass.csv','r') as file, open('hashed_data.csv','w',newline='') as hashfile ,open ('real_pass.csv','w',newline='') as realpassfile:
    
#     hash_dic={}
#     for num in range(1000,10000):
#         hashed_data=hashlib.sha256(str(num).encode('utf-8')).hexdigest()
#         hash_dic[hashed_data]=num
#     writer_hashfile=csv.writer(hashfile)
#     for row in hash_dic.items():
#         writer_hashfile.writerow(row)
        
        
#     hashed_passes={}    
#     reader_file= csv.reader(file)   
#     for row in reader_file:
#         name= row[0]
#         hashed_pas= row[1]
#         for data in hash_dic.keys():
#             if data == hashed_pas :
#                 real_pas= hash_dic[data]
#                 realpassfile.write(f"{name},{real_pas}\n")
