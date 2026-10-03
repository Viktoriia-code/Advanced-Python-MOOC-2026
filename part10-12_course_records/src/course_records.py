class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def update_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade


class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].update_grade(grade)

    def get_course(self, name: str):
        if name not in self.__courses:
            return None

        return self.__courses[name]

    def statistics(self):
        courses = self.__courses.values()

        total_courses = len(self.__courses)
        total_credits = sum(course.credits() for course in courses)
        mean = sum(course.grade() for course in courses) / total_courses

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")

        for grade in range(5, 0, -1):
            count = sum(
                1 for course in self.__courses.values()
                if course.grade() == grade
            )
            print(f"{grade}: {'x' * count}")


class CourseRecordsApplication:
    def __init__(self):
        self.__records = CourseRecords()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        self.__records.add_course(name, grade, credits)

    def get_course(self):
        name = input("course: ")
        course = self.__records.get_course(name)

        if course is None:
            print("no entry for this course")
            return

        print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def execute(self):
        while True:
            print("1 add course")
            print("2 get course data")
            print("3 statistics")
            print("0 exit")

            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.__records.statistics()


application = CourseRecordsApplication()
application.execute()