
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def configure(self):
        pass  # Placeholder method for configuration

class Manager(Employee):
    def configure(self):
        return f"Configuring settings for {self.role} {self.name}: Set up access controls, assign tasks."

class Developer(Employee):
    def configure(self):
        return f"Configuring settings for {self.role} {self.name}: Install necessary development tools, set up repositories."

class Salesperson(Employee):
    def configure(self):
        return f"Configuring settings for {self.role} {self.name}: Provide access to sales systems, set up CRM."