year_one = []
year_two = []

with open('oldest_finalists.txt', 'r') as myfile:
    data_finalists=myfile.readlines()
for data in data_finalists:
	ageindex = (data.find('left">')) + 6
	age = data[ageindex: ageindex + 2]
	if int(age) >= 30:
		yearindexoffset = (data.find('center">'))
		yearindex = (data.find('center">', yearindexoffset + 1)) + 8
		year = data[yearindex: yearindex + 4]
		tdoffset = data.find('<td>') + 1
		tdstart = data.find('<td>', tdoffset)
		tdend = data.find('</td>', tdstart)
		tourny = str(data)[tdstart + 4: tdend]
		val = "%s %s" % (tourny, year)
		if val in year_one:
			year_two.append(val)
		else:
			year_one.append(val)
print year_two