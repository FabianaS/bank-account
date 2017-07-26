#!/usr/bin/python
# -*- coding: utf-8 -*-


class CustomerData:

    def __init__(self, name, personal_id, address, civil_status, email, salary):
        self.name = name
        self.personal_id = personal_id
        self.address = address
        self.civil_status = civil_status
        self.email = email
        self.salary = salary

    def name(self):
        return self.name

    def personal_id(self):
        return self.personal_id

    def address(self):
        return self.address

    def civil_status(self):
        return self.civil_status

    def email(self):
        return self.email

    def salary(self):
        return self.salary
