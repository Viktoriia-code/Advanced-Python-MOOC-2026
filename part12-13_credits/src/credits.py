from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, course: reduced_sum + course.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    courses_grade_1 = list(filter(lambda course : course.grade >= 1, attempts))
    return reduce(lambda reduced_sum, course: reduced_sum + course.credits, courses_grade_1, 0)

def average(attempts: list):
    courses_grade_1 = list(filter(lambda course : course.grade >= 1, attempts))
    return reduce(lambda reduced_sum, course: reduced_sum + course.grade, courses_grade_1, 0)/len(courses_grade_1)