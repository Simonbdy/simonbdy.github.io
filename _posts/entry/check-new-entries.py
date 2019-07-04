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
		no_name = 0
		
		for row in reading:
			if line == 0:
				print("Ignoring first line")
				line += 1
			else:
				
				categories = row[0]
								
				if row[1] == "":
					name_fr = "Aucun nom trouv&#233;"
				else:
					name_fr = row[1].replace("/", "-").replace("?", "Aucun nom trouvé").replace(":","&#58;").replace("é","&#233;")
				
				if row[2] == "":
					name_en = "No name found"
				else:
					name_en = row[2].replace("/", "-").replace("?", "No name found").replace(":","&#58;")
				
				desc_fr = row[4].replace("\n", " <br />").replace(":","&#58;").replace("/", "&#47;")
				desc_en = row[5].replace("\n", " <br />").replace(":","&#58;").replace("/", "&#47;")
				
				if row[6] == "":
					img[0] = ""
				else:
					img[0] = row[6][row[6].rindex("/"):] # prend seulement le nom du fichier et supprime l'adresse
					
				if row[7] == "":
					img[1] = ""
				else:
					img[1] = row[7][row[7].rindex("/"):]
				
				if row[8] == "":
					img[2] = ""
				else:
					img[2] = row[8][row[8].rindex("/"):]
				
				
				if row[9] == "":
					src = ""
				else:
					src = str("<a href=\"" + row[9] + "\" target=\"new\">Source</a>")
					
				line += 1

				filename_date = str("%02d-%02d-%02d-" % (date.year, date.month, date.day-1))
				
				if name_en == "No name found":
					file_title = str("ZZZ-No-name-found-%d" % no_name)
					no_name += 1
				else:
					file_title = name_en
					title = name_en
				
				new_entry = open(filename_date + file_title + ".md", "w+")
				print("Creating file: " + filename_date + file_title + ".md")
				new_entry.write("---" + "\n")
				new_entry.write("layout: post" + "\n")
				new_entry.write("title: " + file_title + "\n")
				new_entry.write("name_fr: " + name_fr + "\n")
				new_entry.write("name_en: " + name_en + "\n")
				new_entry.write("desc_fr: " + desc_fr + "\n")
				new_entry.write("desc_en: " + desc_en + "\n")
				new_entry.write("img: [\"" + img[0] + img[1] + img[2] + "\"]" + "\n")
				new_entry.write("src: " + src + "\n")
				new_entry.write("date: 2019-03-15 17:58:00 +0100" + "\n")# + "%02d-%02d-%02d %02d:%02d:%02d %s" % (date.year, date.month, date.day, date.hour, date.minute-1, date.second, time.timezone) + "\n")
				new_entry.write("categories: [" + categories + "]" + "\n")
				new_entry.write("---" + "\n")
				
				new_line += 1
				
				new_entry.close()
				
		print("Processed %d new entry files." % new_line)
		
if __name__ == "__main__":
	csv_to_md()
