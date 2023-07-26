# Define the class
class Employee:
    name = "Gabriel "
    # Define the method

    def details(self):
        print("Post: RPA Developer")
        print("Department: Tecnology")
        print("Salary: $1000")

# Create the employee object
emp = Employee()

# Print the class variable
print("Name:", emp.name)

# Call the class method
emp.details()