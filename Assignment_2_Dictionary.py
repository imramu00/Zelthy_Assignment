import requests
print("Word?")
word=input()
url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word
json_data = requests.get(url).json()
partOfSpeech = json_data[0]['meanings'][1]['partOfSpeech'].capitalize()
definition = json_data[0]['meanings'][1]['definitions'][0]['definition']
print(partOfSpeech,end=". ")
print(definition,end=". ")