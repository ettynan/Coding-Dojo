# Part 1
users = {
    'students': [{'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'} 
    ]
}


for key, data in users.items():      
    for val in data:
        name = val["first_name"] + " " + val["last_name"]
        print name







