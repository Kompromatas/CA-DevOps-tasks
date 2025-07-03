class Employee:
    def __init__(self, companyname, address, email):
        self.companyname = companyname
        self.address = address
        self.email = email

    def company(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"

class Manager(Employee):    
    def __init__(self, mname, department):
        self.mname = mname
        self.department = department

    def manager_info(self):
        return f"Manager {self.mname} of {self.department} department at {self.companyname}, located at {self.address}. Contact: {self.email}"
    
class Engineer(Employee):
    def __init__(self, ename, specialization):
        self.ename = ename
        self.specialization = specialization

    def engineer_info(self):
        return f"Engineer {self.ename} specializes in {self.specialization} at {self.companyname}, located at {self.address}. Contact: {self.email}"
    
class Intern(Employee):
    def __init__(self, iname, duration):
        self.iname = iname
        self.duration = duration

    def intern_info(self):
        return f"Intern {self.iname} works for {self.duration} months at {self.companyname}, located at {self.address}. Contact: {self.email}"
    
mname = input("Enter manager name: ")
ename = input("Enter engineer name: ")
iname = input("Enter intern name: ")
companyname = ("Karsti Sunys")
address = ("Basanaviciaus 15, Palanga, Lithuania")
email = ("skundai@niekamnerupi.lt") 

manager = Manager(mname, "IT")
manager.companyname = companyname
manager.address = address
manager.email = email   

engineer = Engineer(ename, "Software Development")
engineer.companyname = companyname
engineer.address = address
engineer.email = email

intern = Intern(iname, 6)
intern.companyname = companyname
intern.address = address
intern.email = email    

print(manager.manager_info())
print(engineer.engineer_info())
print(intern.intern_info())
