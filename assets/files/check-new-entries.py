import csv
import time
import datetime

def csv_to_md():

	date = datetime.datetime.today()
	
	file_csv = 'list.csv'

	with open("list.csv", "r") as f:
		reading = csv.reader(f, delimiter=",")

		print("Reading CSV:")

		line = 0
		new_line = 0
		img = ["","",""]
		
		for row in reading:
			if line == 0:
				print("Ignoring first line")
				line += 1
			else:
				print("Line %d:" % line)
				categories = row[0]
				name_fr = row[1]
				name_en = row[2]
				desc_fr = row[4]
				desc_en = row[5]
				img[0] = row[6]
				img[1] = row[7]
				img[2] = row[8]
				src = row[9]
				line += 1

				new_entry = open(name_en + ".md", "w+")
				print("Creating file: " + name_en + ".md")
				new_entry.write("---" + "\n")
				new_entry.write("layout: post" + "\n")
				new_entry.write("title: " + name_en + "\n")
				new_entry.write("name_fr: " + name_fr + "\n")
				new_entry.write("name_en: " + name_en + "\n")
				new_entry.write("desc_fr: " + desc_fr + "\n")
				new_entry.write("desc_en: " + desc_en + "\n")
				new_entry.write("img: [\"" + img[0] + img[1] + img[2] + "\"]" + "\n")
				new_entry.write("src: " + src + "\n")
				new_entry.write("date: " + "%d-%d-%d %d:%d:%d %s" % (date.year, date.month, date.day, date.hour, date.minute, date.second, time.timezone) + "\n")
				new_entry.write("categories: [" + categories + "]" + "\n")
				new_entry.write("---" + "\n")
				
				new_line += 1
				
				new_entry.close()
				
		print('Processed %d new entry files.', new_line)
		
if __name__ == "__main__":
	csv_to_md()
