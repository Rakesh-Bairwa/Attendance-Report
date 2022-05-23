import csv
import pandas as pd
student = {}
n = 24
for x in range(1,n + 1):
	filename = str(x) + ".csv"
	df = pd.read_csv(filename, delimiter = "\t", encoding='utf-16',usecols=["Full Name"])
	store = df.values.tolist()
	data = set()
	for x in range(len(store)):
		if store[x][0] != "Domnic S":
			data.add(store[x][0])

	for key in data:
		if key in student:
			student[key][0] += 1
		else :
			student[key] = [1, 0, 0] # present, absent & percentage
	
for key in student:
	student[key][1] = n - student[key][0]
	student[key][2] = round((student[key][0] / n)*100, 2)
	
output = [[]]
for key in sorted(student.keys()):
	temp = []
	temp.append(key.upper())
	temp.extend(student[key])
	output.append(temp)

with open('output.csv', 'w', newline='') as new_file:
	csv_writer = csv.writer(new_file)
	csv_writer.writerow(["Name","Present","Absent","Percentage"])
	for data in output:	
		csv_writer.writerow(data)
