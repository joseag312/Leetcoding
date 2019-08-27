SELECT FirstName, LastName, City, State
FROM Person p
LEFT JOIN Address a
ON p.PersonId = a.PersonId

/*
This is my 
multiline commment to be recorded
on git
*/