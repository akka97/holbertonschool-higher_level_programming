-- script that lists all cities of a state
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
