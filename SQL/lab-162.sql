CREATE TABLE sys.Restart (
  StudentID INT NOT NULL,
  StudentName VARCHAR(60),
  GraduationDate DATE,
  RestartCity VARCHAR(20),
  PRIMARY KEY (StudentID) 
); 

SET SQL_SAFE_UPDATES = 0;
INSERT INTO sys.Restart
VALUES (0,"John Doe","2020-02-15","Lagos"), (1,"Isaac Newton","2020-12-15","Benin"),
	(2,"Robert Neumann","2021-02-25","Benin"), (3,"Alex Telles","2022-02-15","Lagos"),
	(4,"John Salt","2021-02-25","Benin"), (5,"John Ma","2020-05-24","Lagos"),
	(6,"Emery Gold","2020-05-20","Benin"), (7,"Silver Banon","2020-05-04","Lagos"),
	(8,"Xhen Ji","2020-01-24","Benin"), (9,"Liu Wu","2021-03-14","Lagos");
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM sys.Restart; 



CREATE TABLE sys.Cloud_Practioner (
  StudentID INT NOT NULL,
  CertificationDate DATE,
  PRIMARY KEY (StudentID) 
); 

SET SQL_SAFE_UPDATES = 0;
INSERT INTO sys.Cloud_Practioner 
VALUES (0,"2021-02-15"), (1,"2021-12-15"),
	(2,"2022-02-25"), (3,"2023-02-15"),
	(4,"2022-02-25");
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM sys.Cloud_Practioner;


SELECT cp.StudentID, StudentName, CertificationDate
FROM sys.Cloud_Practioner cp 
INNER JOIN sys.Restart re
USING (StudentID);
-- ON cp.StudentID = re.StudentID;





