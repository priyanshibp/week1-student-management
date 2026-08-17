SELECT * FROM public.students
ORDER BY student_id ASC 

ALTER TABLE students
ADD COLUMN phone VARCHAR(20);

SELECT * FROM students;

ALTER TABLE students
DROP COLUMN height;

SELECT column_name
FROM information_schema.columns
WHERE table_name = 'students'
ORDER BY ordinal_position;