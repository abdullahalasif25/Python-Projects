class User:

    def login(self):
        print('Login Now')

    def register(self):
        print('Register youself')

class Student(User):

    def enroll(self):
        print("Enrollling successful")

    def review(self):
        print("Review for your enrolled courses")

std1 = Student()

std1.login()
std1.register()
std1.enroll()
std1.review()
        
