CREATE TEMP TABLE copy_test2 (id int, name text);
COPY copy_test2 FROM STDIN WITH (FORMAT CSV, HEADER TRUE);
id,name
1,Alice
2,Bob
\.
SELECT * FROM copy_test2;