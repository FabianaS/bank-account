from bank_account_gen.business.params.customer_data import CustomerData

class Customer:

    def __init__(self, customer_data):
        self.name = customer_data.name()
        self.personal_id = customer_data.personal_id()
        self.address = customer_data.address()
        self.marital_status = customer_data.marital_status()
        self.email = customer_data.email()
        self.salary = customer_data.salary()

    def add_account(self, account):
        pass

    def get_account(self, account_num):
        pass

    def as_document(self):
        pass
