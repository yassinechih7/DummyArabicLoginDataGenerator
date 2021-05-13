import random
import csv
import string
import time
import datetime
import configparser

class Person:
	def __init__(self):
		self.id = get_random_string(3)
		self.fullname = genName()
		self.firstname = self.fullname[0]
		self.lastname = self.fullname[1]
		self.email = genEmail(self.fullname, "outlook.com")
		self.password = get_random_string(12)
		self.address = genAdress()
		self.birthdate = getRandomDate()

def genName():
	fileName = "Data/names.csv"
	with open(fileName) as f:
		lines = f.read().splitlines()
		name = random.choices(lines, k=2)
		return name

# Country | City | State | Postal code | Line 2
def genAdress():
	fileName = "Data/cities.csv"
	with open(fileName) as f:
		reader = csv.reader(f)
		street = ["Rue", "Immeuble", "Residence", "Batiment"]
		num = ["N°", "Entree", "Tour", "RS"]

		allcounty = [x for x in reader]
		
		line2 = "{} {}, {} {}".format(random.choice(street), random.randint(0,200),
						  			random.choice(num), random.randint(0,300))

		county = random.choice(allcounty) 
		
		fullAdress = ["Morocco"] + county + [line2]

		return fullAdress

# Return YYYY-MM-DD
def getRandomDate():
	# Using datetime.date to parse random int
	year = random.randint(1980, 1999)
	mounth = random.randint(1, 12)
	day = random.randint(1, 30)
	date=datetime.date(year, mounth, day)
	return date

# Random String generator
def get_random_string(length):
	# choose from all lowercase letter
	letters = string.ascii_lowercase + string.digits 
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str

def genEmail(rname, domain):
	fullName = ''.join(map(str, rname))
	return str(fullName) + str(get_random_string(5)) + "@" + str(domain)

def genConfig():
	p = Person()
	config = configparser.ConfigParser()
	config[p.id] = {
			"firstName": p.firstname,
			"lastName": p.lastname,
			"email": p.email,
			"password": p.password,
			"address": p.address,
			"birthDate": p.birthdate
	}
	with open('info.ini', 'a+') as configfile:
		config.write(configfile)

genConfig()
