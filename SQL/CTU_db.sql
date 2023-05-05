CREATE TABLE `Students` (
  `Student_ID` int PRIMARY KEY,
  `StudentName` varchar(255),
  `ProgramEnrolled` varchar(255),
  `AdvisorID` int
);

CREATE TABLE `Faculty` (
  `Faculty_ID` int PRIMARY KEY,
  `FacultyName` varchar(255),
  `FacultyRank` varchar(255)
);

CREATE TABLE `Courses` (
  `Course_ID` int PRIMARY KEY,
  `CourseName` varchar(255),
  `CreditHours` int,
  `InstructorID` int
);

ALTER TABLE `Faculty` ADD FOREIGN KEY (`Faculty_ID`) REFERENCES `Students` (`AdvisorID`);

ALTER TABLE `Faculty` ADD FOREIGN KEY (`Faculty_ID`) REFERENCES `Courses` (`InstructorID`);
