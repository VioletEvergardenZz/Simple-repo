SELECT DISTINCT department_id FROM employees;

SELECT employee_id,salary AS "月工资",salary*(1+IFNULL(commission_pct,0))*12 AS "年工资",commission_pct FROM employees;

SELECT * FROM `order`;

DESCRIBE countries;

SELECT department_id FROM employees WHERE department_id = 90;
SELECT last_name FROM employees WHERE last_name = 'king';



SELECT 1=NULL,NULL=NULL;
SELECT 1=NULL;
SELECT NULL=NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE commission_pct = NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE commission_pct <=> NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE NOT commission_pct <=> NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE commission_pct IS NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE commission_pct IS NOT NULL;
SELECT last_name,salary,commission_pct FROM employees WHERE ISNULL(commission_pct);


SELECT employee_id,last_name,salary FROM employees WHERE salary BETWEEN 6000 AND 8000; 
SELECT employee_id,last_name,salary FROM employees WHERE salary NOT BETWEEN 6000 AND 8000; 
SELECT employee_id,last_name,salary FROM employees WHERE salary < 6000 OR salary > 8000; 


SELECT last_name,salary,department_id FROM employees WHERE department_id = 10 OR 20 OR 30;
SELECT last_name,salary,department_id FROM employees WHERE department_id = 10 OR department_id = 20 OR department_id = 30 ;
SELECT last_name,salary,department_id FROM employees WHERE department_id IN (10,20,30);

SELECT last_name FROM employees WHERE last_name LIKE '%a%';
SELECT last_name FROM employees WHERE last_name LIKE 'a%';
SELECT last_name FROM employees WHERE last_name LIKE '__a%';
SELECT last_name FROM employees WHERE last_name LIKE '_/_a%';
SELECT last_name FROM employees WHERE last_name LIKE '_$_a%' ESCAPE '$';
SELECT last_name FROM employees WHERE last_name LIKE '%a%' AND last_name LIKE '%e%';
SELECT last_name FROM employees WHERE last_name LIKE '%a%e%' OR '%e%a%';  # 语法错误
SELECT last_name FROM employees WHERE last_name LIKE '%a%e%' OR last_name LIKE '%e%a%';

SELECT last_name,salary,department_id FROM employees WHERE department_id = 50 XOR salary >6000;

SELECT employee_id,salary,salary*12 AS annual_sal FROM employees ORDER BY annual_sal DESC;
SELECT employee_id,salary,salary*12 AS annual_sal FROM employees WHERE annual_sal > 12000 ORDER BY annual_sal DESC;   # 报错
SELECT employee_id,department_id FROM employees WHERE department_id IN (50,60,70) ORDER BY department_id;
SELECT employee_id,department_id,salary FROM employees WHERE department_id IN (50,60,70) ORDER BY department_id DESC,salary ASC; 

# LIMIT (pageNo - 1) * pageSize,pageSize
SELECT employee_id,last_name FROM employees LIMIT 0,20
SELECT employee_id,last_name FROM employees LIMIT 20,20
SELECT employee_id,last_name FROM employees LIMIT 40,20 
SELECT employee_id,last_name,salary FROM employees WHERE salary > 6000 ORDER BY salary DESC LIMIT 10;
# 只显示32,33条数据
SELECT employee_id,last_name FROM employees LIMIT 31,2;
SELECT employee_id,last_name FROM employees LIMIT 2 OFFSET 31;  # MySQL8.0
SELECT employee_id,last_name,salary FROM employees ORDER BY salary DESC LIMIT 1;

DESC employees;
DESC departments;
DESC locations;

SELECT employee_id,department_name FROM employees,departments;  # 笛卡尔积错误,缺少了多表的连接条件
SELECT employee_id,department_name FROM employees,departments WHERE employees.department_id = departments.department_id; # 连接条件
SELECT employees.employee_id,departments.department_name,employees.department_id FROM employees,departments WHERE employees.department_id = departments.department_id;  # 多表查询时,每个字段指明所在的表
SELECT emp.employee_id,dept.department_name,emp.department_id FROM employees emp,departments dept WHERE emp.department_id = dept.department_id; # 别名
SELECT e.employee_id,e.last_name,d.department_name,l.city,e.department_id,d.location_id FROM employees e,departments d,locations l WHERE e.department_id = d.department_id AND d.location_id = l.location_id;  # n个表实现多表查询,则至少需要n-1个连接条件

#非等值连接
SELECT * FROM job_grades;
SELECT e.last_name,e.salary,j.grade_level FROM employees e,job_grades j WHERE e.salary BETWEEN j.lowest_sal AND j.highest_sal ORDER BY salary DESC; 
#自连接
SELECT emp.employee_id,emp.last_name,mgr.employee_id,mgr.last_name FROM employees emp,employees mgr WHERE emp.manager_id = mgr.employee_id;
#内连接
SELECT emp.employee_id,dept.department_name FROM employees emp,departments dept WHERE emp.department_id = dept.department_id;
#SQL99语法实现内连接
SELECT last_name,department_name,city FROM employees e INNER JOIN departments d ON e.department_id = d.department_id JOIN locations l ON d.location_id = l.location_id;
#SQL99语法实现左外连接
SELECT last_name,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id;
#SQL99语法实现右外连接
SELECT last_name,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id;
#SQL99语法实现满外连接
SELECT last_name,department_name FROM employees e FULL JOIN departments d ON e.department_id = d.department_id; # MySQL不支持


# 7种JOIN的实现
#内连接
SELECT employee_id,department_name FROM employees e JOIN departments d ON e.department_id = d.department_id;
#左外连接(左上图)
SELECT employee_id,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id;
#右外连接(右上图)
SELECT employee_id,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id;
#左中图
SELECT employee_id,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL;
#右中图
SELECT employee_id,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL;
#满外连接 左外连接(左上图)+右中图
SELECT employee_id,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id UNION ALL SELECT employee_id,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL;
#满外连接 右外连接(右上图)+左中图
SELECT employee_id,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id UNION ALL SELECT employee_id,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL;
#右下图 左中图+右中图
SELECT employee_id,department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL UNION ALL SELECT employee_id,department_name FROM employees e RIGHT JOIN departments d ON e.department_id = d.department_id WHERE e.department_id IS NULL;



SELECT NOW(),SYSDATE();
SELECT CURDATE(),CURTIME();
SELECT last_name,LENGTH(last_name) "name_length" FROM employees ORDER BY last_name ASC;
SELECT last_name,LENGTH(last_name) "name_length" FROM employees ORDER BY name_length ASC;
SELECT CONCAT(employee_id,',',last_name,',',salary) "OUT_PUT" FROM employees;
SELECT employee_id,DATEDIFF(CURDATE(),hire_date)/365 "worked_years",DATEDIFF(CURDATE(),hire_date) "worked_days" FROM employees ORDER BY worked_years DESC;



SELECT COUNT(employee_id),COUNT(salary),COUNT(salary*2),COUNT(1),COUNT(2),COUNT(*) FROM employees;
SELECT COUNT(commission_pct) FROM employees;
SELECT commission_pct FROM employees WHERE commission_pct IS NOT NULL;
SELECT AVG(salary),SUM(salary)/COUNT(salary) FROM employees;
SELECT AVG(commission_pct) FROM employees;  # 错误的 count不计算空值
SELECT AVG(IFNULL(commission_pct,0)) FROM employees;  # 正确的


SELECT AVG(salary),department_id,SUM(salary) FROM employees GROUP BY department_id;
SELECT job_id,AVG(salary) FROM employees GROUP BY job_id;
SELECT job_id,department_id,AVG(salary) FROM employees GROUP BY department_id,job_id ORDER BY department_id;
SELECT department_id,job_id,AVG(salary) FROM employees GROUP BY department_id;  # 错误的,在SELECT列表中所有未包含在组函数中的列都应该包含在 GROUP BY子句中
SELECT department_id,AVG(salary) FROM employees GROUP BY department_id WITH ROLLUP;
SELECT department_id,AVG(salary) "avg_salary" FROM employees GROUP BY department_id WITH ROLLUP ORDER BY avg_salary ASC;


SELECT department_id,MAX(salary) FROM employees WHERE MAX(salary)>10000 GROUP BY department_id;  # 错误的
SELECT department_id,MAX(salary) FROM employees GROUP BY department_id HAVING MAX(salary)>10000 ; 
SELECT department_id,MAX(salary) FROM employees WHERE department_id IN (20,30,80) GROUP BY department_id HAVING MAX(salary)>12000 ; 



SELECT d.department_name,d.location_id,COUNT(employee_id),AVG(salary) FROM departments d LEFT JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_name,d.location_id ORDER BY AVG(salary) DESC ;


# 子查询
SELECT last_name,salary 
FROM employees
WHERE salary > (
                 SELECT salary
								 FROM employees
								 WHERE last_name = 'Abel'
								 );

# 单行子查询 
# 题目:返回公司工资最少的员工的last_name,job_id和salary
SELECT last_name, job_id, salary
FROM employees
WHERE salary =(
							SELECT MIN(salary)
							FROM employees
							);

# 题目:查询与141号或174号员工的manager_id和department_id相同的其他员工的employee_id,manager_id,department_id
SELECT employee_id, manager_id, department_id
FROM employees
WHERE manager_id IN(
										SELECT manager_id
										FROM employees
										WHERE employee_id IN (174,141))
AND department_id IN(
										 SELECT department_id
										 FROM employees
										 WHERE employee_id IN (174,141))
AND employee_id NOT IN(174,141);

# 题目:查询最低工资大于50号部门最低工资的部门id和其最低工资
SELECT department_id,MIN(salary)
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id
HAVING MIN(salary) > (
											SELECT MIN(salary)
											FROM employees
											WHERE department_id = 50
											);


# 多行子查询
# 题目:返回其它job_id中比job_id为‘IT_PROG’部门所有工资都低的员工的员工号、姓名、job_id以及salary
SELECT employee_id,last_name,job_id,salary 
FROM employees
WHERE job_id <> 'IT_PROG'   # IS NOT 一般用于判断是否为 NULL,而不能用于字符串比较。对于字符串比较,应使用 <> 或 !=
AND salary < ANY(
									SELECT salary
									FROM employees
									WHERE job_id = 'IT_PROG');

# 题目:查询平均工资最低的部门id

SELECT department_id
FROM employees
GROUP BY department_id
HAVING AVG(salary) <= ALL(
												SELECT AVG(salary)
												FROM employees
												GROUP BY department_id
												)
# 空值问题
SELECT last_name
FROM employees
WHERE employee_id NOT IN (
													SELECT manager_id
													FROM employees
													WHERE manager_id IS NOT NULL
													);


# 相关子查询
# 题目:查询员工中工资大于本部门平均工资的员工的last_name,salary和其department_id
SELECT last_name,salary,department_id
FROM employees e1
WHERE salary > (
								SELECT AVG(salary)
								FROM employees e2
								WHERE e2.department_id = e1.department_id
								);

SELECT e.last_name,e.salary,e.department_id
FROM employees e,(
									SELECT department_id,AVG(salary) avg_sal
									FROM employees
									GROUP BY department_id
									) t_dept_avg_sal
WHERE e.department_id = t_dept_avg_sal.department_id
AND e.salary > t_dept_avg_sal.avg_sal;

# 题目:查询员工的id,salary,按照department_name 排序
SELECT employee_id,salary
FROM employees e
ORDER BY(
					SELECT department_name
					FROM departments d
					WHERE e.department_id = d.department_id
					);

# 题目:若employees表中employee_id与job_history表中employee_id相同的数目不小于2,
#       输出这些相同id的员工的employee_id,last_name和其job_id
SELECT employee_id,last_name,job_id
FROM employees e
WHERE 2 <= (
						SELECT COUNT(*)
						FROM job_history j
						WHERE j.employee_id = e.employee_id
						);

# 题目:查询公司管理者的employee_id,last_name,job_id,department_id信息
SELECT DISTINCT mgr.employee_id,mgr.last_name,mgr.job_id,mgr.department_id
FROM employees emp JOIN employees mgr 
ON emp.manager_id = mgr.employee_id;

SELECT employee_id,last_name,job_id,department_id
FROM employees
WHERE employee_id IN (
											SELECT DISTINCT manager_id
											FROM employees
											);

SELECT employee_id,last_name,job_id,department_id
FROM employees e1
WHERE EXISTS (
							SELECT *
							FROM employees e2
							WHERE e1.employee_id = e2.manager_id
							);

# 题目:查询departments表中,不存在于employees表中的部门的department_id和department_name
SELECT d.department_id,d.department_name
FROM departments d LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.department_id is NULL;

SELECT department_id,department_name
FROM departments d
WHERE NOT EXISTS(
									SELECT *
									FROM employees e
 									WHERE e.department_id = d.department_id
									);



  
SELECT DATABASE();
CREATE TABLE IF NOT EXISTS emp1(
id INT,
`name` VARCHAR(15),
hire_date DATE,
salary DOUBLE(10,2)
);
DESC emp1;

# 同时插入多条记录
INSERT INTO emp1(id,salary,`name`)
VALUES(1,1000,'Alice'),(2,2000,'BOb');
SELECT * FROM emp1;
# 将查询结果插入到表中
INSERT INTO emp1(id,`name`,salary)
SELECT employee_id,last_name,salary FROM employees WHERE department_id IN (70,60);
























