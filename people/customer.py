from people.person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, customer_referenceno):
        super().__init__(self, firstname, lastname, customer_referenceno)

        self.customer_referenceno = customer_referenceno

    def get_customerreferenceno(self):
        return self.customer_referenceno

