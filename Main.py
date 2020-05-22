import mysql.connector
#Database name is not implemented until it is created
mydb = mysql.connector.connect(host="localhost", user = "root", passwd = "", database = "Wizards")

mycursor = mydb.cursor()

#Once created, it can be ignored or commented out
mycursor.execute("CREATE DATABASE Wizards")

#Once created it can be ignored or commented out
mycursor.execute("CREATE TABLE Player_Information (id int AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), age smallint UNSIGNED, salary int UNSIGNED, height smallint UNSIGNED, weight smallint UNSIGNED, years smallint UNSIGNED, position VARCHAR(3))")

#Creation of Table within Database
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Bradley", "Beal", 26, 27093019, 75, 207, 7, "SG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Davis", "Bertans", 27, 7000000, 82, 225, 3, "SF"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Isaac", "Bonga", 20, 1416842, 80, 180, 2, "SF"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Troy", "Brown", 26, 27093019, 78, 215, 2, "SF"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Thomas", "Bryant", 22, 8000000, 82, 248, 3, "C"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Rui", "Hachimura", 22, 4469160, 80, 230, 1, "PF"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Ian", "Mahinmi", 33, 15450051, 83, 262, 12, "C"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Garrison", "Matthews", 23, 79568, 77, 215, 1, "SG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Shabazz", "Napier", 28, 1845301, 72, 175, 6, "PG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Anzejs", "Pasecniks", 24, 482144, 85, 220, 1, "C"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Gary", "Payton", 27, 1052909, 75, 195, 4, "PG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Jerome", "Robinson", 23, 3567720, 76, 190, 2, "SG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Admiral", "Schofield", 23, 1000000, 77, 241, 1, "SG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Ish", "Smith", 31, 6000000, 72, 175, 10, "PG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Moritz", "Wagner", 23, 2063520, 83, 245, 2, "SF"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("John", "Wall", 29, 38199000, 76, 210, 9, "PG"))
mycursor.execute("INSERT INTO Player_Information (first_name, last_name, age, salary, height, weight, years, position) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", ("Johnathon", "Williams", 24, 161245 , 81, 228, 1, "PF"))
mydb.commit()
