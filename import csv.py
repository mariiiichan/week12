import csv 

categories = []
canada = []
world = []

with open ('data/OlympicsWinter.csv') as csvfile: 
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader: 
		if line_count is 0: 
			categories.append(row)
			line_count += 1
		elif row [4] == "CAN": 
			canada.append([int(row[0]), row[5], row[6], row[7]])
		else: 
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

	print('total medals for Canada:', len(canada))
	print('total medals for everyone else:', len(world))

	print('processed', line_count, 'rows of data')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada: 
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2004.append(medal)

print('canada won', len(gold_1924), 'gold medals in 1924')
print('canada won', len(gold_1948), 'gold medals in 1948')
print('canada won', len(gold_1972), 'gold medals in 1972')
print('canada won', len(gold_2002), 'gold medals in 2002')
print('canada won', len(gold_2014), 'gold medals in 2014')

# filter 2014 based on gender
# 
# plot a pie chart men vs women =>
# how many medals for each as a percentage of the total 
# 
men = []
women = []

	for gender in 2014

	 	if row [5] == "Men":
	 		men += 1
	 		print(#'men won', len
	 	else row [5] == "Women":
	 		women += 1
	 		print(#print the amount of medals women won in 2014)

totalMedals = len(men) + len(women)

men_percentage = int(len[men])
labels = "Men", "Women", 
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ['gold', 'silver', 'chocolate']
explode = (0.2, 0.1, 0.15)




	
