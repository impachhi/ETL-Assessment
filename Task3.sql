--Task 3
--From Flat file
--Assume a flat file has columns id, name, date_of_birth, salary, and department_id, and the new database has two tables: employees with columns emp_id, full_name, dob, salary, and department_id, and departments with columns dept_id and dept_name.
--Write a SQL query to validate that the data loaded into the new database matches the data from the flat files, including a join with the departments table to ensure department names are correctly associated.

Select emp_id,full_name,dob,salary,department_id from employees e
join departments d on e.department_id=d.dept_id


Note: The final SQL can be crafted after reviewing the mapping document for the column correspondence between the flat file and the database. Additionally, data from the flat file can be read into a DataFrame using Python, allowing for subsequent count or difference validation.

department.d_names mapping?