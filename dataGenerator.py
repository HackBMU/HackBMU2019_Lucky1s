import json

input_file = open('DataJokes/conan.txt', "r").read()
jokes = input_file.split('\n\n')

input_file = open('DataJokes/Sarcasm_Headlines_Dataset.json', "r").read() 
json_array = [json.loads(str(item)) for item in contents.strip().split('\n')]
for item in json_array:
    jokes.append(item['headline'])
    
with open("DataJokes/input.txt", 'w') as f:
    for joke in jokes:
        if str(joke)!='' and str(joke)[-1]!='\n':
            f.write(str(joke) + '\n')
        else:
            f.write(str(joke))
