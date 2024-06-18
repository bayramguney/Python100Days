piano_keys = ["a","b","c","d","e","f","g"]
piano_tuples = ("do","re","mi","fa","so","la","ti")

print(piano_keys[2:5])   # ['c', 'd', 'e']
print(piano_keys[2:5:2])   # ['c', 'e']
print(piano_keys[::2])   # ['a', 'c', 'e', 'g']
print(piano_keys[::-1])   # ['g', 'f', 'e', 'd', 'c', 'b', 'a']


print(piano_tuples[2:5])   # ('mi', 'fa', 'so')
print(piano_tuples[2:5:2])   # ('mi', 'so')
print(piano_tuples[::2])   # ('do', 'mi', 'so', 'ti')
print(piano_tuples[::-1])   # ('ti', 'la', 'so', 'fa', 'mi', 're', 'do')