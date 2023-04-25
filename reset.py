# This is the code to reset all the testing done to the database.

import mysql.connector

mydb = mysql.connector.connect(
        host="sql9.freemysqlhosting.net",
        user="sql9610598",
        password="1Fpa25RFZ1",
        database="sql9610598"
)
# app = Flask(__name__)
#
# app.config["MYSQL_USER"] = 'sql9609926'
# app.config["MYSQL_PASSWORD"] = 'QDmYaixEzt'
# app.config["MYSQL_HOST"] = 'sql9.freemysqlhosting.net'
# app.config["MYSQL_DB"] = 'sql9609926'
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
#
# mysql = MySQL(app)


cur = mydb.cursor()
cur.execute('DROP TABLE Customer_Password')
cur.execute('DROP TABLE Employee_Password')
cur.execute('DROP TABLE Aircraft')
cur.execute('DROP TABLE Aircraft_Specs')
cur.execute('DROP TABLE Ticket_Baggage')
cur.execute('DROP TABLE Baggage')
cur.execute('DROP TABLE Manages')
cur.execute('DROP TABLE Ticket')
cur.execute('DROP TABLE Operates')
cur.execute('DROP TABLE Flight')
cur.execute('DROP TABLE Employee_Age')
cur.execute('DROP TABLE Employee')
cur.execute('DROP TABLE Airport')
cur.execute('DROP TABLE Customer')
cur.execute('DROP TABLE Customer_Age')


cur.execute('''CREATE TABLE Aircraft (Tail_Number VARCHAR(10) PRIMARY KEY,
    Model VARCHAR(50), Creation_Date DATE);''')

cur.execute('''CREATE TABLE Aircraft_Specs (Model VARCHAR(50) PRIMARY KEY,
    Max_Capacity INT, Max_Weight INT, Travel_Distance INT);''')

cur.execute('''CREATE TABLE Airport (Code VARCHAR(3) PRIMARY KEY, Name VARCHAR(50),
    Num_Terminals INT, City VARCHAR(50), Country VARCHAR(50));''')

cur.execute('''CREATE TABLE Customer (ID INT PRIMARY KEY AUTO_INCREMENT, First VARCHAR(50),
    Middle VARCHAR(50), Last VARCHAR(50), DOB DATE, Gender VARCHAR(8), Passport_Number VARCHAR(10),
    Phone_Number VARCHAR(15), Email_Address VARCHAR(100));''')

cur.execute('''CREATE TABLE Customer_Age (DOB DATE PRIMARY KEY, Age INT);''')

cur.execute('''CREATE TABLE Flight (Flight_Number VARCHAR(10), Date DATE, Num_Passengers INT,
    Num_Crew INT, Departure_Time TIME, Arrival_Time TIME, Status VARCHAR(30), Tail_Num VARCHAR(30),
    PRIMARY KEY (Flight_Number, Date));''')

cur.execute('''CREATE TABLE Ticket (ID INT PRIMARY KEY AUTO_INCREMENT, Class VARCHAR(15), Date DATE,
    Seat_Number VARCHAR(5), Num_Bags INT, Cust_ID INT, FlightNum VARCHAR(10),
    FOREIGN KEY (Cust_ID) REFERENCES Customer(ID), FOREIGN KEY (FlightNum) REFERENCES Flight(Flight_Number));''')

cur.execute('''CREATE TABLE Baggage (Baggage_ID INT PRIMARY KEY AUTO_INCREMENT, Weight FLOAT,
    Status VARCHAR(15));''')

cur.execute('''CREATE TABLE Ticket_Baggage (Ticket_ID INT PRIMARY KEY, Baggage_ID INT,
    FOREIGN KEY (Ticket_ID) REFERENCES Ticket(ID), FOREIGN KEY (Baggage_ID) REFERENCES Baggage(Baggage_ID));''')

cur.execute('''CREATE TABLE Employee (ID INT PRIMARY KEY, First VARCHAR(50), Middle VARCHAR(50),
    Last VARCHAR(50), DOB DATE, Gender CHAR(8), Role VARCHAR(50), Wage DECIMAL(10,2), HireDate DATE,
    EmailAddress VARCHAR(100), AirportCode CHAR(3), FOREIGN KEY (AirportCode) REFERENCES Airport(Code));''')

cur.execute('''CREATE TABLE Employee_Age (DOB DATE PRIMARY KEY, Age INT);''')

cur.execute('''CREATE TABLE Manages (TID INT, EID INT, PRIMARY KEY (TID, EID),
    FOREIGN KEY (TID) REFERENCES Ticket(ID), FOREIGN KEY (EID) REFERENCES Employee(ID));''')

cur.execute('''CREATE TABLE Operates (EID INT, FNum VARCHAR(10), PRIMARY KEY (EID, FNum),
    FOREIGN KEY (EID) REFERENCES Employee(ID), FOREIGN KEY (FNum) REFERENCES Flight(Flight_Number));''')

cur.execute('''CREATE TABLE Customer_Password (Cust_ID INT PRIMARY KEY, Password VARCHAR(50), 
    FOREIGN KEY (Cust_ID) REFERENCES Customer(ID));''')

cur.execute('''CREATE TABLE Employee_Password (EID INT PRIMARY KEY, Password VARCHAR(50), 
    FOREIGN KEY (EID) REFERENCES Employee(ID));''')

cur.execute('''INSERT INTO Customer(First, Middle, Last, DOB, Gender, Passport_Number, Phone_Number, Email_Address)
    VALUES ('Ishan', ' ', 'Lamba', '2001-08-13', 'M', '257877968', '202-578-6960', 'ishanlambda23@vt.edu'),
    ('Manasi', ' ', 'Peta', '2002-01-03', 'F', '679093858', '571-425-5306', 'pmanasi24@vt.edu'),
    ('Abigail', 'Meyu', 'Sun', '2001-04-27', 'F', '934672940', '540-388-9539', 'asun14@vt.edu'),
    ('Kylie', 'Marie', 'Simon', '2001-05-21', 'F', '173541908', '757-408-4215', 'ksimon@gmail.com'),
    ('Charles', 'Kente', 'Van Horne', '2000-07-13', 'M', '557263555', '571-321-9418', 'chorne@gmail.com'),
    ('Robert', 'Alexander', 'Vaughn', '2001-02-25', 'M', '926498253', '571-283-1233', 'rvaughn@gmail.com'),
    ('Yoko', 'Jamie', 'Chung', '2001-01-11', 'F', '862807737', '571-342-8469', 'ychung@gmail.com'),
    ('Alex', 'Itachi', 'Haynes', '2001-04-18', 'M', '956733296', '571-943-1239', 'ahaynes@gmail.com'),
    ('Rachelle', ' ', 'Hart', '1999-09-17', 'F', '302436862', '571-239-0324', 'rhart@ymail.com'),
    ('Olivia', 'Faith', 'Cole', '2001-09-04', 'F', '456934591', '540-243-8943', 'ocole@ymail.com'),
    ('Emily', 'Claire', 'Wootten', '2000-10-25', 'F', '283772956', '540-934-9123', 'ewootten@ymail.com'),
    ('Morgan', 'Hope', 'Rodgers', '2001-02-04', 'F', '377921467', '540-345-9546', 'mrodgers@ymail.com'),
    ('Andrew', 'Massimo', 'Ariano', '2000-12-05', 'M', '759896582', '571-345-2349', 'amariano@aol.com'),
    ('Lamia', ' ', 'Kaizer', '2000-12-07', 'F', '293069033', '571-439-1234', 'lkaizer@gmail.com'),
    ('Andrew', 'James', 'Choi', '1998-09-13', 'M', '473242217', '540-143-0254', 'achoi@vt.edu'),
    ('Elizabeth', 'Keilani', 'Britten', '2001-05-22', 'F', '962005482', '540-436-1928', 'lbritt@vt.edu'),
    ('Liling', 'Xie', 'Walsh', '1963-11-22', 'F', '164576867', '540-623-6603', 'lwalsh@gmail.com'),
    ('Joseph', 'Chakwing', 'Sun', '1946-11-15', 'M', '244784778', '843-226-3244', 'jcorjoe@gmail.com'),
    ('Josephine', 'Marie', 'Sun', '1997-01-20', 'F', '106774683', '623-325-0532', 'theylovejo@gmail.com'),
    ('Elite', 'R', 'Joe', '1954-01-01', 'M', '700127530', '123-456-7890', 'elite_joe@yourmom.edu');''')
cur.execute('''INSERT INTO Customer_Age(DOB, Age) VALUES
    ('2001-08-13', '21'),
    ('2002-01-03', '21'),
    ('2001-04-27', '21'),
    ('2001-05-21', '21'),
    ('2000-07-12', '22'),
    ('2001-02-25', '22'),
    ('2001-01-11', '22'),
    ('2001-04-18', '21'),
    ('1999-09-17', '23'),
    ('2001-09-04', '21'),
    ('2000-10-25', '22'),
    ('2001-02-04', '22'),
    ('2000-12-05', '22'),
    ('2000-12-07', '22'),
    ('1998-09-13', '24'),
    ('2001-05-22', '21'),
    ('1963-11-22', '59'),
    ('1946-11-15', '76'),
    ('1997-01-20', '26'),
    ('1954-01-01', '69');''')
cur.execute('''INSERT INTO Baggage(Weight, Status) VALUES
    ('13.05', 'ARRIVED'),
    ('21.53', 'ARRIVED'),
    ('20.90', 'CHECKED-IN'),
    ('30.20', 'ARRIVED'),
    ('43.32', 'CHECKED-IN'),
    ('27.34', 'ARRIVED'),
    ('37.45', 'CHECKED-IN'),
    ('45.34', 'CHECKED-IN'),
    ('34.65', 'CHECKED-IN'),
    ('41.95', 'LOST'),
    ('34.86', 'ARRIVED'),
    ('25.45', 'ARRIVED'),
    ('53.53', 'LOST'),
    ('34.75', 'CHECKED-IN'),
    ('23.67', 'CHECKED-IN'),
    ('54.73', 'ARRIVED'),
    ('23.78', 'ARRIVED'),
    ('32.67', 'CHECKED-IN'),
    ('65.23', 'CHECKED-IN'),
    ('58.35', 'LOST');''')
cur.execute('''INSERT INTO Aircraft (Tail_Number, Model, Creation_Date) VALUES
    ('N452UA', 'Airbus A320-232', '1999-03-15'),
    ('N4888U', 'Airbus A319-131', '2018-06-09'),
    ('N37267', 'Boeing 737-824', '2001-09-02'),
    ('N56859', 'Boeing 757-33N', '2004-04-24'),
    ('N423UA', 'Airbus A320-232', '1995-03-07'),
    ('N8642E', 'Boeing 737-8H4', '2014-07-31'),
    ('HB-JCU', 'Airbus A220-300', '2021-05-24'),
    ('N76503', 'Boeing 737-824', '2006-08-17'),
    ('D-ABYA', 'Boeing 747-830', '2018-06-08'),
    ('N16009', 'Boeing 787-10 Dreamliner', '2019-04-26'),
    ('N653UA', 'Boeing 767-332ER', '1992-10-26'),
    ('N863RW', 'Embraer ERJ-170SE', '2005-10-07'),
    ('N12010', 'Boeing 787-10 Dreamliner', '2019-12-13'),
    ('N649UA', 'Boeing 767-332ER', '1992-07-25'),
    ('D-ABYN', 'Boeing 747-830', '2018-06-08'),
    ('N17015', 'Boeing 767-332ER', '2023-02-10'),
    ('C-FCJZ', 'Bombardier CRJ-900LR', '2018-06-09'),
    ('VT-CIO', 'Airbus A320neo', '2018-06-09'),
    ('N11206', 'Boeing 737-824', '2000-07-25'),
    ('N38424', 'Boeing 737-924ER', '2008-06-30'),
    ('D-AIDC', 'Airbus A321-231', '2018-06-09'),
    ('TC-LSD', 'Airbus A321-271NX', '2019-02-22'),
    ('HS-TEN', 'Airbus A330-343', '2018-06-09'),
    ('9V-SKZ', 'Airbus A380-841', '2018-12-09'),
    ('ZK-MVV', 'ATR 72-600', '2019-09-04'),
    ('ET-AZA', 'Boeing 737 MAX 8', '2022-09-28'),
    ('C-GORN', 'Beechcraft B1900D', '2018-06-10'),
    ('N37502', 'Boeing 737 MAX 9', '2018-06-09');''')
cur.execute('''INSERT INTO Aircraft_Specs (Model, Max_Capacity, Max_Weight, Travel_Distance) VALUES
    ('Airbus A320-232', 180, 178000, 3500),
    ('Airbus A319-131', 128, 171961, 3500),
    ('Boeing 757-33N', 213, 174200, 3900),
    ('Boeing 737-8H4', 175, 154500, 3200),
    ('Airbus A220-300', 145, 149000, 3400),
    ('Boeing 737-824', 181, 174100, 3000),
    ('Boeing 767-332ER', 214, 412000, 5750),
    ('Embraer ERJ-170SE', 70, 85098, 2000),
    ('Boeing 787-10 Dreamliner', 318, 559998, 6300),
    ('Boeing 747-830', 467, 987010, 8500),
    ('Bombardier CRJ-900LR', 86, 81597, 1500),
    ('Airbus A320neo', 162, 174165, 3900),
    ('Airbus A321-231', 205, 206132, 3700),
    ('Airbus A321-271NX', 182, 213848, 4600),
    ('Airbus A330-343', 299, 533519, 7300),
    ('Airbus A380-841', 441, 1267658, 9400),
    ('ATR 72-600', 68, 50706, 850),
    ('Boeing 737 MAX 8', 189, 181200, 4100),
    ('Beechcraft B1900D', 30, 17117, 1180),
    ('Boeing 737 MAX 9', 179, 194302, 3500);''')
cur.execute('''INSERT INTO Flight (Flight_Number, Date, Num_Passengers, Num_Crew, Departure_Time, Arrival_Time, Status, Tail_Num) VALUES
    ('1', '2023-03-21', 150, 6, '10:00', '15:30', 'ARRIVED', 'N8642E'),
    ('2', '2023-03-21', 200, 5, '11:30', '17:00', 'ARRIVED', 'N56859'),
    ('3', '2023-03-22', 200, 6, '09:00', '13:00', 'ARRIVED', 'N649UA'),
    ('4', '2023-03-22', 170, 7, '08:00', '14:00', 'ARRIVED', 'ET-AZA'),
    ('5', '2023-03-22', 160, 6, '21:00', '1:30', 'ARRIVED', 'N37267'),
    ('6', '2023-03-23', 280, 5, '17:30', '22:30', 'DELAYED', 'N12010'),
    ('7', '2023-03-23', 270, 5, '18:30', '23:00', 'IN-FLIGHT', 'N16009'),
    ('8', '2023-03-23', 180, 7, '20:30', '02:30', 'IN-FLIGHT', 'N17015'),
    ('9', '2023-03-24', 160, 5, '06:30', '13:00', 'SCHEDULED', 'N76503'),
    ('10', '2023-03-24', 155, 6, '17:00', '23:00', 'SCHEDULED', 'N38424'),
    ('11', '2023-03-24', 160, 6, '22:00', '03:30', 'SCHEDULED', 'N37502'),
    ('12', '2023-03-25', 145, 5, '09:00', '13:00', 'SCHEDULED', 'N8642E'),
    ('13', '2023-03-25', 205, 7, '08:00', '14:00', 'SCHEDULED', 'N56859'),
    ('14', '2023-03-25', 195, 7, '21:00', '01:30', 'CANCELED', 'N649UA'),
    ('15', '2023-03-26', 165, 5, '17:30', '22:30', 'SCHEDULED', 'ET-AZA'),
    ('16', '2023-03-26', 165, 6, '18:30', '23:00', 'SCHEDULED', 'N37267'),
    ('17', '2023-03-26', 275, 5, '20:30', '02:30', 'SCHEDULED', 'N12010'),
    ('18', '2023-03-27', 275, 5, '06:30', '13:00', 'SCHEDULED', 'N16009'),
    ('19', '2023-03-27', 175, 6, '17:00', '23:00', 'SCHEDULED', 'N17015'),
    ('20', '2023-03-27', 155, 7, '22:00', '03:30', 'SCHEDULED', 'N76503');''')
cur.execute('''INSERT INTO Ticket (Class, Date, Seat_Number, Num_Bags, Cust_ID, FlightNum) VALUES
    ('First', '2023-03-21', '2A', 3, 1, '1'),
    ('Economy', '2023-03-21', '20F', 1, 2, '1'),
    ('Economy', '2023-03-23', '30D', 1, 3, '6'),
    ('Economy', '2023-03-21', '34A', 1, 4, '2'),
    ('Business', '2023-03-23', '13B', 2, 5, '6'),
    ('Economy', '2023-03-21', '21E', 1, 6, '2'),
    ('Business', '2023-03-23', '12C', 2, 7, '6'),
    ('Economy', '2023-03-23', '26B', 1, 8, '7'),
    ('Economy', '2023-03-23', '32A', 1, 9, '7'),
    ('Business', '2023-03-22', '10D', 2, 10, '3'),
    ('Economy', '2023-03-22', '21D', 1, 11, '3'),
    ('Economy', '2023-03-22', '36C', 1, 12, '4'),
    ('Economy', '2023-03-22', '33F', 1, 13, '4'),
    ('Business', '2023-03-23', '12B', 2, 14, '7'),
    ('Business', '2023-03-23', '9A', 2, 15, '8'),
    ('Economy', '2023-03-22', '26E', 1, 16, '5'),
    ('Economy', '2023-03-22', '23C', 1, 17, '5'),
    ('Economy', '2023-03-23', '26F', 1, 18, '8'),
    ('Economy', '2023-03-23', '31D', 1, 19, '8'),
    ('Business', '2023-03-22', '14C', 2, 20, '5');''')
cur.execute('''INSERT INTO Airport (Code, Name, Num_Terminals, City, Country) VALUES 
    ('AMS', 'Amsterdam Airport Schiphol', 4, 'Amsterdam', 'Netherlands'),
    ('ATL', 'Hartsfield-Jackson Atlanta International Airport', 7, 'Atlanta', 'United States'),
    ('BKK', 'Suvarnabhumi Airport', 7, 'Bangkok', 'Thailand'),
    ('CAI', 'Cairo International Airport', 2, 'Cairo', 'Egypt'),
    ('CDG', 'Charles de Gaulle Airport', 4, 'Paris', 'France'),
    ('DXB', 'Dubai International Airport', 3, 'Dubai', 'United Arab Emirates'),
    ('EZE', 'Ministro Pistarini International Airport', 2, 'Buenos Aires', 'Argentina'),
    ('FCO', 'Leonardo da Vinci�Fiumicino Airport', 4, 'Rome', 'Italy'),
    ('FRA', 'Frankfurt Airport', 2, 'Frankfurt', 'Germany'),
    ('GRU', 'S�o Paulo�Guarulhos International Airport', 3, 'S�o Paulo', 'Brazil'),
    ('HND', 'Haneda Airport', 3, 'Tokyo', 'Japan'),
    ('ICN', 'Incheon International Airport', 2, 'Seoul', 'South Korea'),
    ('IST', 'Istanbul Airport', 4, 'Istanbul', 'Turkey'),
    ('JFK', 'John F. Kennedy International Airport', 6, 'New York', 'United States'),
    ('JNB', 'OR Tambo International Airport', 2, 'Johannesburg', 'South Africa'),
    ('LAX', 'Los Angeles International Airport', 8, 'Los Angeles', 'United States'),
    ('LHR', 'Heathrow Airport', 5, 'London', 'United Kingdom'),
    ('MAD', 'Adolfo Su�rez Madrid�Barajas Airport', 4, 'Madrid', 'Spain'),
    ('MEX', 'Benito Juarez International Airport', 2, 'Mexico City', 'Mexico'),
    ('PEK', 'Beijing Capital International Airport', 3, 'Beijing', 'China'),
    ('SFO', 'San Francisco International Airport', 4, 'San Francisco', 'United States'),
    ('SYD', 'Sydney Airport', 3, 'Sydney', 'Australia'),
    ('YVR', 'Vancouver International Airport', 3, 'Vancouver', 'Canada'),
    ('YYZ', 'Toronto Pearson International Airport', 2, 'Toronto', 'Canada');''')
cur.execute('''INSERT INTO Ticket_Baggage(Ticket_ID, Baggage_ID) VALUES
    ('1', '10'),
    ('2', '7'),
    ('3', '20'),
    ('4', '18'),
    ('5', '19'),
    ('6', '8'),
    ('7', '2'),
    ('8', '9'),
    ('9', '15'),
    ('10', '14'),
    ('11', '16'),
    ('12', '3'),
    ('13', '1'),
    ('14', '4'),
    ('15', '5'),
    ('16', '6'),
    ('17', '11'),
    ('18', '13'),
    ('19', '12'),
    ('20', '17');''')
cur.execute('''INSERT INTO Employee (ID, First, Middle, Last, DOB, Gender, Role, Wage, HireDate, EmailAddress, AirportCode) VALUES 
    (1, 'Wilfred', 'Elliot', 'Trengove', '1967-01-23', 'Male', 'Pilot', '90', '2014-05-26', 'wetrengrove@airline.com', NULL),
    (2, 'Robert', NULL, 'Sangster', '1968-03-09', 'Male', 'Pilot', '88', '2014-11-16', 'rsangster@airline.com', NULL),
    (3, 'Flora', 'Eleanore', 'Ford', '1968-06-09', 'Female', 'Pilot', '86', '2016-02-04', 'feford@airline.com', NULL),
    (4, 'Cyril', 'Buck', 'Sharp', '1968-07-04', 'Male', 'Pilot', '84', '2016-04-03', 'cbsharp@airline.com', NULL),
    (5, 'Jolie', NULL, 'Toller', '1971-03-14', 'Female', 'Pilot', '82', '2017-10-09', 'jtoller@airline.com', NULL),
    (6, 'Cecilia', 'Elfrieda', 'Atterberry', '1972-06-25', 'Female', 'Pilot', '80', '2019-04-22', 'ceatterberry@airline.com', NULL),
    (7, 'Jameson', 'Alger', 'Leigh', '1974-06-06', 'Male', 'Pilot', '78', '2019-11-26', 'jaleigh@airline.com', NULL),
    (8, 'Demetria', 'Coral', 'Caulfield', '1974-11-27', 'Female', 'Pilot', '76', '2020-02-23', 'dccaulfield@airline.com', NULL),	
    (9, 'Travis', NULL, 'Sudworth', '1978-06-03', 'Male', 'Pilot', '74', '2020-07-25', 'tsudworth@airline.com', NULL),
    (10, 'Knox', NULL, 'Ilbert', '1979-08-31', 'Male', 'Pilot', '72', '2020-09-20', 'kilbert@airline.com', NULL),
    (11, 'Irwin', 'Gavin', 'Richard', '1980-10-23', 'Male', 'Pilot', '70', '2022-01-31', 'igrichard@airline.com', NULL),
    (12, 'Amy', 'Finley', 'Bond', '1987-02-23', 'Female', 'Pilot', '68', '2022-07-26', 'afbond@airline.com', NULL),
    (13, 'Rachel', NULL, 'James', '1976-07-12', 'Female', 'Cabin Crew', '37', '2014-07-14', 'rjames@airline.com', NULL),	
    (14, 'Christopher', 'Basil', 'Elwin', '1966-02-23', 'Male', 'Cabin Crew', '39', '2015-07-29', 'cbelwin@airline.com', NULL),
    (15, 'Olivia', 'Ellen', 'Belmont', '1981-12-01', 'Female', 'Cabin Crew', '43', '2015-10-01', 'oebelmont@airline.com', NULL),
    (16, 'Emmit', 'Quinten', 'Deighton', '1983-12-05', 'Male', 'Cabin Crew', '47', '2015-10-12', 'eqdeighton@airline.com', NULL),
    (17, 'Brandt', 'Flint', 'Snelling', '1981-10-06', 'Male', 'Cabin Crew', '45', '2015-10-24', 'bfsnelling@airline.com', NULL),
    (18, 'Scott', NULL, 'Moore', '1965-03-12', 'Male', 'Cabin Crew', '42', '2016-04-12', 'smoore@airline.com', NULL),
    (19, 'Kelly', 'Regena', 'Hunter', '1993-09-08', 'Female', 'Cabin Crew', '46', '2017-02-24', 'kghunter@airline.com', NULL),	
    (20, 'Eldon', 'Kelley', 'Stephens', '1970-08-02', 'Male', 'Cabin Crew', '43', '2018-03-18', 'ekstephens@airline.com', NULL),
    (21, 'Sabrina', NULL, 'Bull', '1977-09-17', 'Female', 'Cabin Crew', '36', '2018-10-16', 'sbull@airline.com', NULL),
    (22, 'Adeline', NULL, 'Blakeslee', '1974-11-20', 'Female', 'Cabin Crew', '41', '2018-10-23', 'ablakeslee@airline.com', NULL),
    (23, 'Barrett', 'Darren', 'Church', '1993-10-30', 'Male', 'Cabin Crew', '40', '2019-04-05', 'bdchurch@airline.com', NULL),
    (24, 'Ashley', 'Laraine', 'Marlowe', '1993-01-19', 'Female', 'Cabin Crew', '35', '2019-05-06', 'almarlowe@airline.com', NULL),	
    (25, 'Brook', 'Cory', 'Ramsey', '1972-10-10', 'Male', 'Cabin Crew', '45', '2019-05-07', 'bcramsey@airline.com', NULL),
    (26, 'Garth', NULL, 'Moore', '1978-01-03', 'Male', 'Cabin Crew', '42', '2019-07-22', 'gmoore@airline.com', NULL),
    (27, 'Zane', NULL, 'Remington', '1988-07-28', 'Male', 'Cabin Crew', '36', '2019-11-04', 'zremington@airline.com', NULL),	
    (28, 'Loreen', NULL, 'Hubert', '1968-06-12', 'Female', 'Cabin Crew', '44', '2021-01-06', 'lhubert@airline.com', NULL),
    (29, 'Allyn', 'Sunday', 'Henderson', '1982-08-18', 'Female', 'Cabin Crew', '41', '2021-03-02', 'ashenderson@airline.com', NULL),	
    (30, 'Clifton', NULL, 'Bush', '1993-01-22', 'Male', 'Cabin Crew', '42', '2021-04-14', 'cbush@airline.com', NULL),
    (31, 'Deena', 'Marina', 'Cash', '1970-07-05', 'Female', 'Cabin Crew', '47', '2021-06-08', 'dmcash@airline.com', NULL),	
    (32, 'Hunter', NULL, 'Francis', '1975-09-05', 'Male', 'Cabin Crew', '37', '2021-06-14', 'hfrancis@airline.com', NULL),
    (33, 'Homer', 'Denis', 'Merrill', '1992-07-03', 'Male', 'Cabin Crew', '43', '2021-11-21', 'hdmerrill@airline.com', NULL),
    (34, 'Landon', 'Corey', 'Mills', '1973-10-20', 'Male', 'Cabin Crew', '47', '2022-01-29', 'lcmills@airline.com', NULL),
    (35, 'Tera', 'Palmer', 'Macy', '1966-02-17', 'Female', 'Cabin Crew', '46', '2022-10-13', 'tpmacy@airline.com', NULL),
    (36, 'Brent', NULL, 'Jack', '1974-10-19', 'Male', 'Cabin Crew', '40', '2022-12-23', 'bjack@airline.com', NULL),
    (37, 'Trinity', 'Enola', 'Palmer', '1987-07-30', 'Female', 'Cabin Crew', '35', '2014-03-20', 'tepalmer@airline.com', NULL),	
    (38, 'Maya', NULL, 'Herberts', '1992-11-15', 'Female', 'Cabin Crew', '45', '2014-03-26', 'mherberts@airline.com', NULL),
    (39, 'Donald', 'Samson', 'Platt', '1993-06-30', 'Male', 'Cabin Crew', '39', '2014-04-10', 'dsplatt@airline.com', NULL),
    (40, 'Lorayne', 'Roxanna', 'Thompkins', '1974-03-11', 'Female', 'Cabin Crew', '47', '2014-04-26', 'lrthompkins@airline.com', NULL),	
    (41, 'Monroe', 'Nathan', 'Thompsett', '1975-10-13', 'Male', 'Cabin Crew', '42', '2015-04-23', 'mnthompsett@airline.com', NULL),
    (42, 'Lawson', 'Irvine', 'Marshall', '1986-01-26', 'Male', 'Cabin Crew', '39', '2015-05-02', 'limarchall@airline.com', NULL),
    (43, 'Ethan', NULL, 'Lowell', '1976-07-18', 'Male', 'Cabin Crew', '42', '2015-05-31', 'elowell@airline.com', NULL),
    (44, 'Dorothy', NULL, 'Waller', '1984-08-08', 'Female', 'Cabin Crew', '37', '2015-07-23', 'dwaller@airline.com', NULL),	
    (45, 'Jasmine', 'Morgan', 'Statham', '1970-07-03', 'Female', 'Cabin Crew', '38', '2015-10-27', 'jmstatham@airline.com', NULL),	
    (46, 'Nolan', 'Noah', 'Travers', '1976-07-13', 'Male', 'Cabin Crew', '36', '2016-06-29', 'nntravers@airline.com', NULL),
    (47, 'Maryanne', 'Elizabeth', 'Key', '1994-11-11', 'Female', 'Cabin Crew', '39', '2017-10-31', 'mekey@airline.com', NULL),
    (48, 'Burke', NULL, 'Delano', '1977-12-05', 'Male', 'Cabin Crew', '35', '2017-11-22', 'bdelano@airline.com', NULL),
    (49, 'Antony', 'Riley', 'Barber', '1982-08-14', 'Male', 'Cabin Crew', '41', '2019-01-13', 'arbarber@airline.com', NULL),	
    (50, 'Harvie', NULL, 'Horsfall', '1969-06-08', 'Male', 'Cabin Crew', '37', '2019-03-16', 'hhorsfall@airline.com', NULL),
    (51, 'Aimee', NULL, 'Leach', '1988-02-02', 'Female', 'Ticket Manager', '30', '2019-04-08', 'aleach@airline.com', NULL),
    (52, 'Dixon', NULL, 'Kingston', '1967-06-17', 'Male', 'Ticket Manager', '27', '2020-09-17', 'dkingston@airline.com', NULL),
    (53, 'Wendy', 'Clarice', 'Patrick', '1978-09-04', 'Female', 'Ticket Manager', '30', '2021-03-04', 'wcpatrick@airline.com', NULL),	
    (54, 'Anna', 'Susan', 'Giffard', '1994-11-05', 'Female', 'Ticket Manager', '26', '2021-04-07', 'asgiffard@airline.com', NULL),
    (55, 'Alton', 'Granville', 'Frank', '1969-12-15', 'Male', 'Ground Staff', '30', '2021-08-09', 'agfrank@airline.com', 'JFK'),
    (56, 'Rosemarie', NULL, 'Stern', '1976-12-07', 'Female', 'Ground Staff', '27', '2022-03-26', 'rstern@airline.com', 'ATL'),
    (57, 'Marlin', 'Omar', 'West', '1984-09-16', 'Male', 'Ground Staff', '29', '2022-04-07', 'mowest@airline.com', 'JFK'),
    (58, 'Lloyd', 'Brook', 'Pound', '1976-06-06', 'Male', 'Ground Staff', '27', '2022-06-02', 'lbpound@airline.com', 'LAX'),
    (59, 'Norman', NULL, 'Foster', '1994-11-18', 'Male', 'Ground Staff', '28', '2022-06-12', 'nfoster@airline.com', 'ATL'),
    (60, 'Carissa', 'Rosa', 'Cantrell', '1971-03-05', 'Female', 'Ground Staff', '29', '2022-08-12', 'crcantrell@airline.com', 'LAX'),
    (61, 'Sharon', NULL, 'Tittensor', '1976-02-16', 'Female', 'Ground Staff', '27', '2022-11-01', 'stittensor@airline.com', 'JFK'),
    (62, 'Oswald', NULL, 'Gorbold', '1982-11-06', 'Male', 'Ground Staff', '24', '2014-02-21', 'ogorbold@airline.com', 'SFO'),
    (63, 'Sybil', 'Terra', 'Durand', '1983-07-11', 'Female', 'Ground Staff', '25', '2014-07-18', 'stdurand@airline.com', 'SFO'),
    (64, 'Ryan', NULL, 'Royston', '1991-02-24', 'Male', 'Ground Staff', '27', '2014-09-17', 'rroyston@airline.com', 'ATL'),
    (65, 'Steven', 'Spencer', 'Winslow', '1968-10-19', 'Male', 'Ground Staff', '28', '2015-06-05', 'sswinslow@airline.com',	'JFK'),
    (66, 'Bryan', 'Robert', 'Cason', '1985-10-21', 'Male', 'Ground Staff', '25', '2015-08-03', 'brcason@airline.com',	'LAX'),
    (67, 'Kathlyn', 'Arden', 'Sandford', '1979-02-26', 'Female', 'Ground Staff', '29', '2016-01-28', 'kasandford@airline.com', 'ATL'),
    (68, 'Nelson', NULL, 'Shofield', '1970-01-20', 'Male', 'Ground Staff', '27', '2016-02-06', 'nshofield@airline.com', 'JFK'),
    (69, 'Brian', NULL, 'Goodman', '1960-02-07', 'Male', 'Admin', '100', '2010-02-06', 'bgoodman@airline.com', NULL);''')
cur.execute('''INSERT INTO Operates (EID, FNum) VALUES
    (1, '1'),
    (2, '1'),
    (13, '1'),
    (14, '1'),
    (15, '1'),
    (16, '1'),
    (3, '2'),
    (4, '2'),
    (17, '2'),
    (18, '2'),
    (19, '2'),
    (5, '3'),
    (6, '3'),
    (20, '3'),
    (21, '3'),
    (22, '3'),
    (23, '3'),
    (7, '4'),
    (8, '4'),
    (24, '4'),
    (25, '4'),
    (26, '4'),
    (27, '4'),
    (28, '4'),
    (9, '5'),
    (10, '5'),
    (29, '5'),
    (30, '5'),
    (31, '5'),
    (32, '5'),
    (11, '6'),
    (12, '6'),
    (33, '6'),
    (34, '6'),
    (35, '6'),
    (1, '7'),
    (2, '7'),
    (36, '7'),
    (37, '7'),
    (38, '7'),
    (3, '8'),
    (4, '8'),
    (39, '8'),
    (40, '8'),
    (41, '8'),
    (42, '8'),
    (43, '8'),
    (5, '9'),
    (6, '9'),
    (44, '9'),
    (45, '9'),
    (46, '9'),
    (7, '10'),
    (8, '10'),
    (47, '10'),
    (48, '10'),
    (49, '10'),
    (50, '10'),
    (9, '11'),
    (10, '11'),
    (13, '11'),
    (14, '11'),
    (15, '11'),
    (16, '11'),
    (11, '12'),
    (12, '12'),
    (17, '12'),
    (18, '12'),
    (19, '12'),
    (1, '13'),
    (2, '13'),
    (20, '13'),
    (21, '13'),
    (22, '13'),
    (23, '13'),
    (24, '13'),
    (3, '14'),
    (4, '14'),
    (25, '14'),
    (26, '14'),
    (27, '14'),
    (28, '14'),
    (29, '14'),
    (5, '15'),
    (6, '15'),
    (30, '15'),
    (31, '15'),
    (32, '15'),
    (7, '16'),
    (8, '16'),
    (33, '16'),
    (34, '16'),
    (35, '16'),
    (36, '16'),
    (9, '17'),
    (10, '17'),
    (37, '17'),
    (38, '17'),
    (39, '17'),
    (11, '18'),
    (12, '18'),
    (40, '18'),
    (41, '18'),
    (42, '18'),
    (1, '19'),
    (2, '19'),
    (43, '19'),
    (44, '19'),
    (45, '19'),
    (46, '19'),
    (3, '20'),
    (4, '20'),
    (47, '20'),
    (48, '20'),
    (49, '20'),
    (50, '20'),
    (13, '20');''')
cur.execute('''INSERT INTO Manages (TID, EID) VALUES
    (1, 51),
    (2, 52),
    (3, 53),
    (4, 54),
    (5, 51),
    (6, 52),
    (7, 53),
    (8, 54),
    (9, 51),
    (10, 52),
    (11, 53),
    (12, 54),
    (13, 51),
    (14, 52),
    (15, 53),
    (16, 54),
    (17, 51),
    (18, 52),
    (19, 53),
    (20, 54);''')
cur.execute('''INSERT INTO Employee_Age (DOB, Age) VALUES
    ('1967-01-23', 56), 
    ('1968-03-09', 55), 
    ('1968-06-09', 54), 
    ('1968-07-04', 54), 
    ('1971-03-14', 52), 
    ('1972-06-25', 50), 
    ('1974-06-06', 48), 
    ('1974-11-27', 48), 
    ('1978-06-03', 44), 
    ('1979-08-31', 43), 
    ('1980-10-23', 42), 
    ('1987-02-23', 36), 
    ('1976-07-12', 46), 
    ('1966-02-23', 57), 
    ('1981-12-01', 41), 
    ('1983-12-05', 39),
    ('1981-10-06', 41), 
    ('1965-03-12', 58), 
    ('1993-09-08', 29), 
    ('1970-08-02', 52), 
    ('1977-09-17', 35), 
    ('1974-11-20', 48),
    ('1993-10-30', 29), 
    ('1993-01-19', 30), 
    ('1972-10-10', 50), 
    ('1978-01-03', 45), 
    ('1988-07-28', 34), 
    ('1968-06-12', 54), 
    ('1982-08-18', 40), 
    ('1993-01-22', 30), 
    ('1970-07-05', 52), 
    ('1975-09-05', 47), 
    ('1992-07-03', 30), 
    ('1973-10-20', 49), 
    ('1966-02-17', 57), 
    ('1974-10-19', 48), 
    ('1987-07-30', 35), 
    ('1992-11-15', 30), 
    ('1993-06-30', 29), 
    ('1974-03-11', 49), 
    ('1975-10-13', 47), 
    ('1986-01-26', 37), 
    ('1976-07-18', 46), 
    ('1984-08-08', 38), 
    ('1970-07-03', 52), 
    ('1976-07-13', 46), 
    ('1994-11-11', 28), 
    ('1977-12-05', 35), 
    ('1982-08-14', 40), 
    ('1969-06-08', 53), 
    ('1988-02-02', 34), 
    ('1967-06-17', 55), 
    ('1978-09-04', 44), 
    ('1994-11-05', 28), 
    ('1969-12-15', 53), 
    ('1976-12-07', 46), 
    ('1984-09-16', 38), 
    ('1976-06-06', 46), 
    ('1994-11-18', 28), 
    ('1971-03-05', 52), 
    ('1976-02-16', 47), 
    ('1982-11-06', 40), 
    ('1983-07-11', 39), 
    ('1991-02-24', 32), 
    ('1968-10-19', 54), 
    ('1985-10-21', 37), 
    ('1979-02-26', 44), 
    ('1970-01-20', 53);''')

cur.execute('''INSERT INTO Employee_Password (EID, Password) VALUES
    (1, 'abcd'),
    (2, 'efgh'),
    (3, 'ijkl'),
    (4, 'mnop'),
    (5, 'qrst'),
    (6, 'uvwx'),
    (7, 'yzab'),
    (8, 'cdef'),
    (9, 'ghij'),
    (10, 'klmn'),
    (11, 'opqr'),
    (12, 'stuv'),
    (13, 'wxyza'),
    (14, 'bcde'),
    (15, 'fghi'),
    (16, 'jklm'),
    (17, 'nopq'),
    (18, 'rstu'),
    (19, 'vwxy'),
    (20, 'zabc'),
    (21, 'defg'),
    (22, 'hijk'),
    (23, 'lmno'),
    (24, 'pqrs'),
    (25, 'tuvw'),
    (26, 'xyzab'),
    (27, 'hfwf'),
    (28, 'ewhf'),
    (29, 'hwfiw'),
    (30, 'iewfwi'),
    (31, 'fiweuh'),
    (32, 'wieufk'),
    (33, 'weof'),
    (34, 'uehfa'),
    (35, 'hbwcwk'),
    (36, 'rfawfdk'),
    (37, 'wefhb'),
    (38, 'weuf'),
    (39, 'wefn'),
    (40, 'kfbka'),
    (41, 'wiefhn'),
    (42, 'wefab'),
    (43, 'wkejfk'),
    (44, 'wakefb'),
    (45, 'awkefn'),
    (46, 'wihr'),
    (47, 'kearfbsv'),
    (48, 'krfakwef'),
    (49, 'efbhakw'),
    (50, 'ekwrhf'),
    (51, 'wufhaw'),
    (52, 'weirf'),
    (53, 'kfndfb'),
    (54, 'wer'),
    (55, 'kjwejfhiw'),
    (56, 'iewrhu'),
    (57, 'ahwef'),
    (58, 'owefahf'),
    (59, 'werhw'),
    (60, 'alwirehu'),
    (61, 'yesafn'),
    (62, 'wjherfi'),
    (63, 'ebfal'),
    (64, 'wekhrf'),
    (65, 'fblaekhwe'),
    (66, 'lahifba'),
    (67, 'wrhfaf'),
    (68, 'password');''')

cur.execute('''INSERT INTO Customer_Password (Cust_ID, Password) VALUES
    (1, 'abcd'),
    (2, 'efgh'),
    (3, 'ijkl'),
    (4, 'mnop'),
    (5, 'qrst'),
    (6, 'uvwx'),
    (7, 'yzab'),
    (8, 'cdef'),
    (9, 'ghij'),
    (10, 'klmn'),
    (11, 'opqr'),
    (12, 'stuv'),
    (13, 'wxyza'),
    (14, 'bcde'),
    (15, 'fghi'),
    (16, 'jklm'),
    (17, 'nopq'),
    (18, 'rstu'),
    (19, 'vwxy'),
    (20, 'zabc');''')

cur.execute('COMMIT;')
mydb.close()




