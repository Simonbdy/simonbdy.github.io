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
				
				categories_fr = row[2].split(", ")
				categories_en = row[3].split(", ")
								
				if row[0] == "":
					name_fr = "Aucun nom trouv&#233;"
				else:
					name_fr = row[0].replace("/", "-").replace("?", "Aucun nom trouvé").replace(":","&#58;").replace("é","&#233;")
				
				if row[1] == "":
					name_en = "No name found"
				else:
					name_en = row[1].replace("/", "-").replace("?", "No name found").replace(":","&#58;")
				
				desc_fr = row[4].replace("\n", " ").replace(":","&#58;").replace("/", "&#47;")
				desc_en = row[5].replace("\n", " ").replace(":","&#58;").replace("/", "&#47;")
				
				# prend seulement le nom du fichier et supprime l'adresse avant le premier "/" par la droite

				if row[6] == "":
					img[0] = None
				else:
					if "/" not in row[6]:
						img[0] = img[0] = row[6]
					else:						
						img[0] = row[6][row[6].rindex("/"):].replace("/", "")

				if row[7] == "":
					img[1] = None
				else:
					if "/" not in row[7]:
						img[1] = img[1] = row[7]
					else:						
						img[1] = row[7][row[7].rindex("/"):].replace("/", "")

				if row[8] == "":
					img[2] = None
				else:
					if "/" not in row[8]:
						img[2] = img[2] = row[8]
					else:						
						img[2] = row[8][row[8].rindex("/"):].replace("/", "")
									
				# Transforme la source en lien
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
					file_title = name_en.replace(" ", "_").replace("\n", "_")
					title = name_en
				
				new_entry = open(filename_date + file_title + ".md", "w+")
				print("Creating file " + filename_date + file_title + ".md from file " + file_csv + ", line " + str(new_line+2))
				new_entry.write("---" + "\n")
				new_entry.write("layout: post" + "\n")
				new_entry.write("title: " + file_title + "\n")
				new_entry.write("name_fr: " + name_fr + "\n")
				new_entry.write("name_en: " + name_en + "\n")
				new_entry.write("desc_fr: " + desc_fr + "\n")
				new_entry.write("desc_en: " + desc_en + "\n")

				# avoid broken empty image links
				if img[2] == None:
					if img[1] == None:
						if img[0] == None:
							new_entry.write("img: []" + "\n")
						else:
							new_entry.write("img: [\"" + img[0] + "\"]" + "\n")
					else:
						new_entry.write("img: [\"" + img[0] + "\", \"" + img[1] + "\"]" + "\n")
				else:
					new_entry.write("img: [\"" + img[0] + "\", \"" + img[1] + "\", \"" + img[2] + "\"]" + "\n")

				new_entry.write("src: " + src + "\n")
				new_entry.write("date: 2019-03-15 17:58:00 +0100" + "\n")# This doesn't work in the Jekyll regeneration of the site, why? "date: %02d-%02d-%02d %02d:%02d:%02d %s" % (date.year, date.month, date.day, date.hour, date.minute-1, date.second, time.timezone) + "\n")
					
				a = ["FR_" + s for s in categories_fr] + ["EN_" + s for s in categories_en]
				new_entry.write("categories: " + str(a).replace("\'", "") + "\n")

				# new_entry.write("categories_en: " + categories_en + "\n")
				new_entry.write("---" + "\n")
				
				new_line += 1
				
				new_entry.close()
				
		print("Processed %d new entry files." % new_line)
		
if __name__ == "__main__":
	csv_to_md()
