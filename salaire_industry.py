class Employee():

    def __init__(self, firstName, familyName, age, entranceYear, workMeasure):
        self.familyName = familyName
        self.firstName = firstName
        self.age = age
        self.entranceYear = entranceYear
        self.workMeasure = workMeasure
        self.riskyWorkBonus = None
        self.bonus = None
        self.wmToSalaryRate = None

        # Nous savons que chaque employé devra avoir une méthode getSalary

    # mais nous n'avons aucune raison de spécifier ici la façon de le calculer.
    # L'usage du décorateur @abstractmethod obligera les classes fille à faire
    # un choix d'implémentation.

    def getSalary(self):
        salary = self.workMeasure * self.wmToSalaryRate + self.bonus + self.riskyWorkBonus
        return salary

    def __str__(self):
        return "L'employé {} {} a un salaire de {} €".format(self.firstName,
                                                             self.familyName,
                                                             int(self.getSalary()))

class Salesman(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, turnover):
        super().__init__(familyName, firstName, age, entranceYear, turnover)
        self.riskyWorkBonus = 0
        self.bonus = 400
        self.wmToSalaryRate = 0.2
class Representant(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, turnover):
        super().__init__(familyName, firstName, age, entranceYear, turnover)
        self.riskyWorkBonus = 0
        self.bonus = 800
        self.wmToSalaryRate = 0.2
class Producer(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, producedUnits):
        super().__init__(familyName, firstName, age, entranceYear, producedUnits)
        self.riskyWorkBonus = 0
        self.bonus = 0
        self.wmToSalaryRate = 5
class Wharehouseman(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, houresDone):
        super().__init__(familyName, firstName, age, entranceYear, houresDone)
        self.riskyWorkBonus = 0
        self.bonus = 0
        self.wmToSalaryRate = 65
class ProducerWithRisk(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, producedUnits):
        super().__init__(familyName, firstName, age, entranceYear, producedUnits)
        self.riskyWorkBonus = 200
        self.bonus = 0
        self.wmToSalaryRate = 5
class WharehousemanWithRisk(Employee):

    def __init__(self, familyName, firstName, age, entranceYear, houresDone):
        super().__init__(familyName, firstName, age, entranceYear, houresDone)
        self.riskyWorkBonus = 200
        self.bonus = 0
        self.wmToSalaryRate = 65

class Staff:
    def __init__(self):
        self.listEmployees = []

    def add(self, e):
        self.listEmployees.append(e)

    def displaySalaries(self):
        for e in self.listEmployees:
            print(e)  # == print(e.__str__())

    def displayAverageSalary(self):
        averageSalary = 0
        for e in self.listEmployees:
            averageSalary += e.getSalary()
        averageSalary /= len(self.listEmployees)
        print(int(averageSalary))

myEmployees = Staff()
myEmployees.add(Salesman("Pierre", "Business", 45, "1995", 30000))
myEmployees.add(Representant("Léon", "Ventout", 25, "2001", 20000))
myEmployees.add(Producer("Yves", "Ahalouest", 28, "1998", 1000))
myEmployees.add(Wharehouseman("Jeanne", "Stoktout", 32, "1998", 45))
myEmployees.add(ProducerWithRisk("Jean", "Flippe", 28, "2000", 1000))
myEmployees.add(WharehousemanWithRisk("Al", "Abordage", 30, "2001", 45))

myEmployees.displaySalaries()
myEmployees.displayAverageSalary()
