--1. Find Departments with Average Salary Greater than a Certain Amount
SELECT d.dept_id,d.dept_name,AVG(e.salary) AS avg_salary FROM employees e
JOIN departments d ON e.department_id = d.dept_id
GROUP BY d.dept_idp
HAVING AVG(e.salary) > 50000;

--2. List Employees with Salaries Above the Department Average and Working on More Than One Project

SELECT e.emp_id, e.full_name, e.salary, d.dept_name FROM employees e
JOIN departments d ON e.department_id = d.dept_id
JOIN ( SELECT ep.emp_id FROM employee_projects ep GROUP BY ep.emp_id HAVING COUNT(ep.project_id) > 1
) AS emp_proj ON e.emp_id = emp_proj.emp_id
WHERE e.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e.department_id
);

--3. Find Employees with the Highest Salary in Each Department and List Their Projects

SELECT e.emp_id, e.full_name, e.salary, e.department_id,p.project_name,p.project_id FROM employees e
JOIN (
        SELECT department_id, MAX(salary) AS max_salary
        FROM employees
        GROUP BY department_id
    ) AS max_salaries ON e.department_id = max_salaries.department_id AND e.salary = max_salaries.max_salary
join employee_projects ep ON e.emp_id = ep.emp_id
join projects p ON ep.project_id = p.project_id