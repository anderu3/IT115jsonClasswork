# importing json
import json

# initializing the data dictionary

data = {

    'name': 'Andrew Lee',
    'age': 21,
    'city': 'Lynnwood, WA',
    'interests':['Tennis','League of Legends','TFT','Valorant','Music','Golf'],
    'is_student': True

}

# create json file and write the  contents to the json file
with open('data.json','w') as json_file:

        json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

# reading contents of previously created data_dict json_file

with open('data.json','r') as json_file:
        
        # create object loaded_data to use into later argument
        loaded_data = json.load(json_file)

# prints "Succesfully able to read data.json" when successfully reading data.json
print("Succesfully able to read data.json")

# prints the loaded data from json_file from earlier initialization
print(loaded_data)

# update data_dict with new values from keys
loaded_data['age'] = 28
loaded_data['interests'].append('Aviation')

# open data.json file and write the updated data to the file
with open('data.json','w') as json_file:

        json.dump(loaded_data,json_file,indent=4)

print("Data has been rewritten to data.json")