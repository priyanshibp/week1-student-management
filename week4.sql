SELECT * FROM public.students
ORDER BY student_id ASC 

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

INSERT INTO courses (course_name)
VALUES
    ('Python'),
    ('SQL'),
    ('Web Development'),
    ('Data Science');

	SELECT * FROM courses;

	CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);

SELECT student_id, name
FROM students
ORDER BY student_id;

INSERT INTO enrollments (student_id, course_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 1),
    (4, 3),
    (5, 4);

	SELECT * FROM enrollments;

	SELECT
    students.name,
    courses.course_name
FROM students
INNER JOIN enrollments
    ON students.student_id = enrollments.student_id
INNER JOIN courses
    ON enrollments.course_id = courses.course_id;

	SELECT
    students.name,
    courses.course_name
FROM students
LEFT JOIN enrollments
    ON students.student_id = enrollments.student_id
LEFT JOIN courses
    ON enrollments.course_id = courses.course_id
ORDER BY students.student_id;

INSERT INTO enrollments (student_id, course_id)
VALUES (99, 1);

SELECT
    students.student_id,
    students.name,
    courses.course_name
FROM students
LEFT JOIN enrollments
    ON students.student_id = enrollments.student_id
LEFT JOIN courses
    ON enrollments.course_id = courses.course_id
ORDER BY students.student_id;