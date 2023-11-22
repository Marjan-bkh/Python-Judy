import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as file , open(output_file_name,'w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg= mean(grade_list)
            final_list.append([name,avg])    
        writer = csv.writer(out)
        writer.writerows(final_list)
            
    

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as file , open(output_file_name,'w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg=mean(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(item[1],item[0]))}
        # sorted_avg= dict(sorted(dic.items(), key=lambda item:item[1]))
        writer = csv.writer(out)
        for row in sorted_avg.items():
            writer.writerow(row)


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name,'r') as file , open(output_file_name,'w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg=mean(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(-item[1],item[0]))}
        top3=dict(list(sorted_avg.items())[:3])
        writer = csv.writer(out)
        for row in top3.items():
            writer.writerow(row)



def calculate_three_worst(input_file_name, output_file_name):
    
    with open(input_file_name,'r') as file , open(output_file_name,'w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg=mean(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        sorted_avg={key:value for key,value in sorted(dic.items(), key=lambda item:(item[1],item[0]))}
        floor3=list(sorted_avg.values())[:3]
        writer = csv.writer(out)
        for item in floor3:
            writer.writerow([item])


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as file , open(output_file_name,'w', newline='') as out:
        reader= csv.reader(file)
        final_list=[]
        dic={}
        for row in reader:
            name=row[0]
            grade_list=[float(grade) for grade in row[1:]]
            avg=mean(grade_list)
            final_list.append([name,avg])  
            dic[name] =avg
        list_avg= list(dic.values())
        try:
            avg_avg= [mean(list_avg)]
        except ZeroDivisionError:
            avg_avg= []   
        writer = csv.writer(out)
        for item in avg_avg:
            writer.writerow([item])
            
            
