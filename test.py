import random
import csv

l_names = ['Nicholson', 'Blevins', 'Pontigua', 'Lucero', 'Hays', 'Bhaji', 'Aguilar', 'Whitehead', 'Perry', 'Meyers',
           'Camacho', 'Insaf', 'Ashley', 'Wilson', 'Kaiser', 'Lin', 'Marsh', 'Leonard', 'Rocha', 'Haney', 'Atkinson',
           'Hamilton', 'Bird', 'Hansen', 'Tanner']

f_names = ['Kirstyn', 'Toby', 'Jacoby', 'Daysha', 'Melissa', 'Melina', 'Guillermo',
           'Donovan', 'Josh', 'Josef', 'Hector', 'Kaycee', 'Cristobal', 'Keegan', 'Daylon',
           'Terrance', 'Lexie', 'Piper', 'Alia', 'Jazmine', 'Dangelo', 'Victor',
           'Clifton', 'Estefany', 'Benny', 'Hasan', 'Jesenia', 'Vaughn', 'Corinne', 'Emiliano']
min_age = 17
max_age = 45
domain_name = ['google.com',  'yahoo.com',  'hotmail.com',  'waverly.org']
likes_cookies = ['yes',  'no']

num_students = 20

students = []

for i in range(num_students):
    l_names_len = len(l_names)
    if l_names_len > 1:
        rand_name_index = random.choice(range(0, l_names_len))
        rand_l_name = l_names[rand_name_index]
        rand_f_name = f_names[rand_name_index]
        rand_age = random.choice(range(min_age, max_age))
        rand_domain_index = random.choice(range(0, len(domain_name)))
        rand_email = f"{rand_f_name}_{rand_l_name[0]}@{domain_name[rand_domain_index]}"
        rand_cookie_index = random.choice(range(0, 2))
        rand_cookie = likes_cookies[rand_cookie_index]
        students.append((rand_l_name, rand_f_name, rand_age, rand_email, rand_cookie))
        l_names.remove(rand_l_name)
        f_names.remove(rand_f_name)

print(students)
print(len(students))

filename = "student_names.csv"
with open(filename, 'w') as test_file:
    file_writer = csv.writer(test_file)
    for student_detail in students:
        file_writer.writerow(student_detail)

