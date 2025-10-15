# Inheritance (KALITIM)

# Kalıtım bir class'ın başka bir class'ın özelliklerini almasıdır.
# tek yönlüdür

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person created")

    def whoami(self):
        print(f"I am {self.firstname}")

class Student(Person):
    def __init__(self, fname, lname, id):
        Person.__init__(self, fname, lname)
        self.number = id    # Bu student'a özgü bir özelliktir Person tarafından kullanılamaz.

        print("Student created")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def whoami(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Veli", "NAMLI")    
s1 = Student("Nuri", "Ilman", "2235076066" )    #ID gibi üzerinde matematiksel işlem yapılmayacak olan bilgileri string olarak tutmak daha güvenlidir.  
t1 = Teacher("Ayşe", "Güney", "Fen")

p1.whoami()
s1.whoami()
t1.whoami()

print(s1.number)