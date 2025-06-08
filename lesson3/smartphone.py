class Smartphone:
    def __init__(self, company, model, number):
        self.company = company
        self.model = model
        self.number = number

    def get_company(self):
        return self.company

    def get_model(self):
        return self.model

    def get_number(self):
        return self.number
