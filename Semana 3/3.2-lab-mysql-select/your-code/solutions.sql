------CHALLENGE 1------
SELECT authors.au_id AS 'AUTHOR ID',
concat(authors.au_lname," ", authors.au_fname) AS 'FULLNAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLISHER'
FROM authors

INNER JOIN titleauthor
ON titleauthor.au_id = authors.au_id
INNER JOIN titles
ON titles.title_id = titleauthor.title_id
INNER JOIN publishers
ON publishers.pub_id = titles.pub_id;

------CHALLENGE 2------

SELECT authors.au_id AS 'AUTHOR ID',
concat(authors.au_lname," ", authors.au_fname) AS 'FULLNAME',
publishers.pub_name AS 'PUBLISHER',
COUNT(titles.title) AS 'TITLE COUNT'
FROM authors


INNER JOIN titleauthor
ON titleauthor.au_id = authors.au_id
INNER JOIN titles
ON titles.title_id = titleauthor.title_id
INNER JOIN publishers
ON publishers.pub_id = titles.pub_id
GROUP BY publishers.pub_id, authors.au_id;

------CHALLENGE 3------

SELECT authors.au_id AS 'AUTHOR ID',
concat(authors.au_lname," ", authors.au_fname) AS 'FULLNAME',
SUM(sales.qty) AS 'TOTAL'
FROM authors

INNER JOIN titleauthor
ON titleauthor.au_id = authors.au_id
INNER JOIN titles
ON titles.title_id = titleauthor.title_id
INNER JOIN sales
ON sales.title_id = titles.title_id

GROUP BY authors.au_id
ORDER BY TOTAL DESC
LIMIT 3;

------CHALLENGE 4------

SELECT authors.au_id AS 'AUTHOR ID',
concat(authors.au_lname," ", authors.au_fname) AS 'FULLNAME',
IFNULL(SUM(sales.qty),0) AS 'TOTAL' 
FROM authors

/*
Now we need to use left join instead of inner join because we have to include the authors who have sold 0 titles, and with the inner join the only authors whom appear
would be the common authors of the tables, who are, the authors who have sold at least 1 title
*/

LEFT JOIN titleauthor
ON titleauthor.au_id = authors.au_id
LEFT JOIN titles
ON titles.title_id = titleauthor.title_id
LEFT JOIN sales
ON sales.title_id = titles.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC
LIMIT 23;

--BONUS--

SELECT authors.au_id AS 'AUTHOR ID',
concat(authors.au_lname," ", authors.au_fname) AS 'FULLNAME',
concat(IFNULL(SUM(titles.advance + titles.ytd_sales * titles.price * titles.royalty/100), 0), '$') AS PROFIT
FROM authors