CREATE DATABASE IF NOT EXISTS Library;
USE Library;

CREATE TABLE IF NOT EXISTS BookRecord (
    BNo VARCHAR(20) PRIMARY KEY,
    BName VARCHAR(100) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    Publisher VARCHAR(100),
    Qty INT DEFAULT 0,
    DateOfPurchase DATE
);

CREATE TABLE IF NOT EXISTS Member (
    MNo VARCHAR(20) PRIMARY KEY,
    MName VARCHAR(100) NOT NULL,
    Mobile VARCHAR(20),
    DateOfMembership DATE,
    Address VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS IssueRecord (
    IssueID INT AUTO_INCREMENT PRIMARY KEY,
    BNo VARCHAR(20),
    MNo VARCHAR(20),
    IssueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (BNo) REFERENCES BookRecord(BNo) ON DELETE CASCADE,
    FOREIGN KEY (MNo) REFERENCES Member(MNo) ON DELETE CASCADE
);

INSERT IGNORE INTO BookRecord VALUES
('B101', 'Python Programming', 'Reema Thareja', 450.00, 'Oxford', 5, '2023-08-01'),
('B102', 'Database Management System', 'Korth', 550.00, 'McGraw Hill', 3, '2023-08-05');

INSERT IGNORE INTO Member VALUES
('M101', 'Kartik', '9999999999', '2023-08-10', 'Saharanpur');
