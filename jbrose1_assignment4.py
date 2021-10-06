import csv

student_name = "Justin Brose"

sum_city = 0
num_city = 0

sum_hwy = 0
num_hwy = 0

sum_f_hwy = 0
num_f_hwy = 0

sum_s_city = 0
num_s_city = 0

ford_hwy = 0
suv_city = 0
avg_city = 0
avg_hwy = 0

with open('mpg.csv') as file:
    mpg_reader = csv.DictReader(file)
    for row in mpg_reader:
        if int(row['cty']) > 0:
            sum_city = int(row['cty']) + sum_city
            num_city += 1
            avg_city = sum_city/num_city
        if int(row['hwy']) > 0:
            num_hwy += 1
            sum_hwy = sum_hwy + int(row['hwy'])
            avg_hwy = sum_hwy/num_hwy
        if row['manufacturer'] == "ford":
            sum_f_hwy = int(row['hwy']) + sum_f_hwy
            num_f_hwy += 1
            ford_hwy = sum_f_hwy/num_f_hwy
        if row['class'] == "suv":
            sum_s_city = int(row['cty']) + sum_s_city
            num_s_city += 1
            suv_city = sum_s_city/num_s_city
            with open('jbrose1_assignment4.txt', 'w') as text:
                text.write("This is the average city mpg: " + str(avg_city) + "\n")
                text.write("This is the average highway mpg: " + str(avg_hwy) + "\n")
                text.write("This is the average for highway mpg: " + str(ford_hwy) + "\n")
                text.write("This is the average suv city mpg: " + str(suv_city) + "\n")
