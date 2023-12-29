
Drop table IF EXISTS olympics_copy;
CREATE TABLE olympics_copy AS SELECT * FROM olympics;
DELETE FROM olympics_copy;

DO $$
Declare i int := 0;
Declare number_test_rows int := 10;
BEGIN
	LOOP
		EXIT When i > (number_test_rows-1);
		INSERT INTO olympics_copy
		VALUES (i + 2000, 'CITY №' || (i + 1));
		i:= i+1;
	END LOOP;
END;
$$;

-- select * from olympics_copy;