SELECT MAX(Sel.Salary) AS [SecondHighestSalary]
FROM
(
    SELECT  
        Salary,
        DENSE_RANK() OVER (ORDER BY Salary DESC) AS dr
    FROM Employee 
) AS Sel
WHERE Sel.dr = 2