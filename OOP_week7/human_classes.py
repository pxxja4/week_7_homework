
class Person:
    def __init__(self, firstname, lastname, age, gender, nationality):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__gender = gender
        self.__nationality = nationality

    def get_attributes(self):
        return {
            "firstname": self.__firstname,
            "lastname": self.__lastname,
            "age": self.__age,
            "gender":  self.__gender,
            "nationality": self.__nationality,
    }

    def __str__(self):
        return (
                f"First name: {self.__firstname}\n"
                f"Lastname: {self.__lastname}\n"
                f"Age: {self.__age}\n"
                f"Gender: {self.__gender}\n"
                f"Nationality: {self.__nationality}\n"
        )


class Employee(Person):
    def __init__(self, firstname, lastname,gender, departament, band, ID):
        super().__init__(firstname, lastname, age=None, gender=gender, nationality=None)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__department = departament
        self.__band = band
        self.__ID = ID

    def get_attributes(self):
        attributes = super().get_attributes()
        attributes.pop("age")
        attributes.pop("nationality")
        attributes["ID"] = self.__ID
        attributes["Band"] = self.__band
        attributes["Department"] = self.__department


    def __str__(self):
        return (f"First name: {self._Person__firstname}\n"
                f"Lastname: {self._Person__lastname}\n"
                f"Gender: {self._Person__gender}\n"
                f"Department: {self._Employee__department}\n"
                f"Band: {self._Employee__band}\n"
                f"Employee ID: {self._Employee__ID}")


class Customer(Person):
    def __init__(self, firstname, gender, age, product_purchased):
        super().__init__(firstname, lastname=None, age=age, gender=gender, nationality=None)
        self.__firstname = firstname
        self.__age = age
        self.__gender = gender
        self.__product_purchased = product_purchased


    def get_attributes(self):
        attributes = super().get_attributes()
        attributes.pop("lastname")
        attributes.pop("nationality")
        attributes["Purchased item"] = self.__product_purchased

    def __str__(self):
        return (f"First name: {self._Person__firstname}\n"
                f"Age: {self._Person__age}\n"
                f"Gender: {self._Person__gender}\n"
                f"Purchased item: {self._Customer__product_purchased}\n")


