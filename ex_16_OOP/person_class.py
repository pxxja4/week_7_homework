class Person:
    # we instantiate a class by using the constructor __init__
    #  we define some attribute to the class as parameters
    def __init__(self, firstname, lastname, age, gender, nationality):
        self.firstname = firstname
        self._lastname = lastname
        self.__age = age
        self.__gender = gender
        self.nationality = nationality

    # functions within a class are called methods
    # they represent behaviours
    def get_personal_details(self):
        return self.firstname.upper(), self._lastname.upper()

    def get_person_passport_details(self):
        return self.nationality, self.__gender, self.__age

    def set_personal_details(self, firstname, lastname):
        if str(self.firstname).isalpha() and str(self._lastname).isalpha():
            self.firstname = firstname
            self._lastname = lastname
        else:
            # instantiatiing a ValueError object and throwing
            raise ValueError('personal details must be alphabetic')

        # Setter for age with validation
    def set_age(self, age):
            self.__age = self.validate_age(age)

        # Getter for age
    def get_age(self):
            return self.__age

        # Private method to validate age
    def validate_age(age):
        if isinstance(age, int) and age > 0:
                return age
        else:
                raise ValueError("Age must be a positive integer")

    def __str__(self):
        # overrides an inherited method
        return f" Here is the person_1 details: {self.firstname.upper()}, {self._lastname.upper()} , {self.__age}"

