CREATE TABLE "User_Table" (
	"UserID"	INTEGER NOT NULL,
	"Username"	TEXT,
	"Password"	TEXT,
	"Forename"	TEXT,
	"Surname"	TEXT,
	"Email"	TEXT,
	"DateOfBirth"	TEXT,
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE "DriverTable" (
	"DriverID"	INTEGER NOT NULL,
	"DriverFName"	TEXT,
	"DriverSName"	TEXT,
	"DriverPhone"	TEXT,
	"DriverGender"	TEXT,
	PRIMARY KEY("DriverID" AUTOINCREMENT)
);

CREATE TABLE "BookingsTable" (
	"BookingID"	INTEGER NOT NULL,
	"CarTransmition"	TEXT,
	"BookingCar"	TEXT,
	"BookingDate"	TEXT,
	"BookingTime"	TEXT,
	"BookedDate"	INTEGER,
	"LessonType"	TEXT,
	"UserID"	INTEGER,
	"DriverID"	INTEGER,
	FOREIGN KEY("DriverID") REFERENCES "DriverTable"("DriverID"),
	FOREIGN KEY("UserID") REFERENCES "User_Table"("UserID"),
	PRIMARY KEY("BookingID")
);