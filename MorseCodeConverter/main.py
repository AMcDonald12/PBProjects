import pandas

#Create dictionary from csv data
mcodecsv = pandas.read_csv('mcode_convert.csv')
mcodelist = mcodecsv.to_dict(orient="split")
mcodedict = {}

for i in range(len(mcodelist['data'])):
    mcodedict[mcodelist['data'][i][0]] = mcodelist['data'][i][1]

#Translation process
phrase = input('Enter what you would like translated to Morse Code: ').upper()
characters = []
for i in phrase:
    characters.append(i)
translated = []
for i in characters:
    try:
        translated.append(mcodedict[i])
    except KeyError:
        pass
string = ""
for i in translated:
    string += i + " "
print(string)