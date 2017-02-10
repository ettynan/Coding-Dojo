# Part 1

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'} 
# ]


# for student in students:      
#     print student["first_name"] + " " + student["last_name"]
        

# Part 2

users = {
    'Students': [{'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'} 
    ],
    'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

for key, data in users.items():      
    print key
    index = 0
    for val in data:
        name = val["first_name"].upper() + " " + val["last_name"].upper()
        index += 1
        print index, "-", name, "-", len(name)-1



