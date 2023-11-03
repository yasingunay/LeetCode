# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName,Address.city,
    Address.state from Person LEFT JOIN Address on Person.personID = Address.personId