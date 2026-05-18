# SQL Tips

## Order of operations
An important thing to learn when using SQL is the order of operation. It helps to get an idea of the runtime of a query and most importantly know how we should structure it.
The order is as follows
```sql
FROM --(and JOIN)
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```
**So let's say we select `column1` as `col_1`, we can't use the alias in the `WHERE` clause.**
**!!! In some languages, we can use aliases created in SELECT in the GROUP BY !!!**

## WHERE vs HAVING
WHERE filters rows before grouping while having filters it after. That's why we can't use for example avg(col) in a where clause most of the time because the group by did not happen yet. If we need the average of a column without grouping by we need to have a select subquery that returns it.

## Correlated subquery vs JOIN subquery
There are a lot of common problems that can be solved in multiple ways.
A classic example is this: Let's say we have a table employees(id, name, department, salary) and we want to get the employees that have more than the average salary in their respective departments.

### Correlated subquery
```sql
select * from employees e1 where e1.salary > (select avg(salary) from employees e2 where e1.department = e1.department)
```
In this method, the subquery has access to the current row that is being processed by the main query that's why we can have `e1.department` in the subquery.

### JOIN
```sql
select * from employees e1 inner join
(select department, avg(salary) as dep_avg from employees group by department) e2 on
e1.department = e2.department where e1.salary > dep_avg
```
In this method, we compute all the department's averages in the table e2 then we join it on the initial table (on department) and just check if the salary is higher than the average.

Those 2 methods have the same output, it is the time complexity that differs depending on the number of department and employees. The first method computes the average of the current's employee department everytime, while the second one computes the averages once.

## Old join syntax
When performing joins, sometimes we can see the following syntax:
```sql
select * from e1,e2 where e1.id = e2.id
```
this is an implicit way of doing an inner join but it is not encouraged.

## CASE WHEN
A classic example of queries is conditional queries as such:
```sql
SELECT
    COUNT(*) AS total_orders,
    SUM(
        CASE
            WHEN status = 'completed' THEN 1
            ELSE 0
        END
    ) AS completed_orders
FROM orders;
```