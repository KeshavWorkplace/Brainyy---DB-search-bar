import sqlite3

# connect to sqlite
connection = sqlite3.connect("Employee.db")


# create a cursor to perform insert, update and delete record
cursor = connection.cursor()

# create a table
table_info = '''
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Position VARCHAR(50),
    HireDate DATE,
    Salary DECIMAL(10, 2)
)
'''

cursor.execute(table_info)
cursor.execute(
    '''
INSERT INTO Employee (EmployeeID, FirstName, LastName, Department, Position, HireDate, Salary)
VALUES
    (1, 'John', 'Doe', 'IT', 'Developer', '2022-01-10', 60000.00),
    (2, 'Jane', 'Smith', 'HR', 'HR Specialist', '2022-02-15', 55000.00),
    (3, 'Mike', 'Johnson', 'Marketing', 'Marketing Coordinator', '2022-03-20', 62000.00),
    (4, 'Sara', 'Williams', 'IT', 'System Analyst', '2022-04-25', 58000.00),
    (5, 'David', 'Brown', 'Finance', 'Accountant', '2022-05-30', 65000.00),
    (6, 'Emily', 'Jones', 'HR', 'Recruiter', '2022-06-05', 60000.00),
    (7, 'Daniel', 'Taylor', 'IT', 'Software Engineer', '2022-07-10', 70000.00),
    (8, 'Olivia', 'Miller', 'Marketing', 'Graphic Designer', '2022-08-15', 55000.00),
    (9, 'Ethan', 'Moore', 'Finance', 'Financial Planner', '2022-09-20', 62000.00),
    (10, 'Sophia', 'Davis', 'HR', 'Training Specialist', '2022-10-25', 58000.00),
    (11, 'Liam', 'Wilson', 'IT', 'Database Administrator', '2022-11-30', 65000.00),
    (12, 'Ava', 'Smith', 'Marketing', 'Marketing Manager', '2022-12-05', 70000.00),
    (13, 'Noah', 'Johnson', 'Finance', 'Senior Financial Analyst', '2023-01-10', 75000.00),
    (14, 'Isabella', 'Brown', 'HR', 'HR Manager', '2023-02-15', 80000.00),
    (15, 'Mia', 'Anderson', 'IT', 'Lead Developer', '2023-03-20', 90000.00),
    (16, 'James', 'White', 'Marketing', 'Content Creator', '2023-04-25', 55000.00),
    (17, 'Sophie', 'Martinez', 'Finance', 'Investment Analyst', '2023-05-30', 62000.00),
    (18, 'Jackson', 'Hall', 'HR', 'HR Director', '2023-06-05', 70000.00),
    (19, 'Lily', 'Baker', 'IT', 'Software Architect', '2023-07-10', 80000.00),
    (20, 'Logan', 'Ward', 'Marketing', 'Social Media Specialist', '2023-08-15', 60000.00),
    (21, 'Aiden', 'Morris', 'Finance', 'Financial Controller', '2023-09-20', 75000.00),
    (22, 'Emma', 'Harris', 'HR', 'Compensation Analyst', '2023-10-25', 58000.00),
    (23, 'Carter', 'Morgan', 'IT', 'DevOps Engineer', '2023-11-30', 68000.00),
    (24, 'Grace', 'Garcia', 'Marketing', 'Brand Manager', '2023-12-05', 72000.00),
    (25, 'Henry', 'Lopez', 'Finance', 'Senior Accountant', '2024-01-10', 78000.00),
    (26, 'Zoe', 'Perez', 'HR', 'Employee Relations Specialist', '2024-02-15', 60000.00),
    (27, 'Gabriel', 'Turner', 'IT', 'UI/UX Designer', '2024-03-20', 85000.00),
    (28, 'Ella', 'Cooper', 'Marketing', 'Digital Marketing Specialist', '2024-04-25', 62000.00),
    (29, 'Elijah', 'Wright', 'Finance', 'Budget Analyst', '2024-05-30', 70000.00),
    (30, 'Avery', 'Fisher', 'HR', 'Benefits Administrator', '2024-06-05', 58000.00),
    (31, 'Mason', 'Simmons', 'IT', 'Front-end Developer', '2024-07-10', 75000.00),
    (32, 'Aria', 'Ferguson', 'Marketing', 'SEO Specialist', '2024-08-15', 62000.00),
    (33, 'Caleb', 'Hunter', 'Finance', 'Tax Analyst', '2024-09-20', 68000.00),
    (34, 'Scarlett', 'Newton', 'HR', 'HR Coordinator', '2024-10-25', 60000.00),
    (35, 'Wyatt', 'Hill', 'IT', 'Backend Developer', '2024-11-30', 80000.00),
    (36, 'Nova', 'Rhodes', 'Marketing', 'Event Coordinator', '2024-12-05', 65000.00),
    (37, 'Grayson', 'Ford', 'Finance', 'Financial Adviser', '2025-01-10', 72000.00),
    (38, 'Aurora', 'Sullivan', 'HR', 'Talent Acquisition Specialist', '2025-02-15', 58000.00),
    (39, 'Leo', 'Riley', 'IT', 'Systems Engineer', '2025-03-20', 78000.00),
    (40, 'Luna', 'Chavez', 'Marketing', 'Public Relations Specialist', '2025-04-25', 68000.00);

'''
)
# inserting records


# display all the records
print('Inserted Data')
data = cursor.execute('Select count(*) from Employee')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
