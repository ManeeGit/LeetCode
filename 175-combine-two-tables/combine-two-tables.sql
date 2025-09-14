/* Write your PL/SQL query statement below */


SELECT firstname, lastname, city , state FROM Person left Join Address on Person.personId = Address.personId;
