#!/usr/bin/python
# -*- coding: utf-8 -*-
from mongoengine import *
from werkzeug.security import safe_str_cmp
from flask import jsonify
from bank_account_gen.security.entropy import gen_salt, compute_hash
import datetime

# ======================================================================================================
# CLASS BANK ACCOUNT AUTHORIZED PERSON
# ======================================================================================================
class BankAccountAuthorizedPerson(EmbeddedDocument):
    """
        Esto define la clase que representa una persona autorizada para realizar retiros de la cuenta
        bancaria
    """

    # Cedula del autorizado
    personal_id = StringField(max_length=30, required=True)

    # Nombre completo del autorizado
    full_name = StringField(max_length=80, required=True)

    # Direccion del autorizado
    address = StringField(max_length=256, required=True)

    # Monto maximo que puede retirar diariamente
    max_ammount = DecimalField(required=True)

# ======================================================================================================
# CLASS BANK ACCOUNT
# ======================================================================================================
class BankAccount(EmbeddedDocument):

    """
        Esto representa una cuenta bancaria que pertenece a un cliente bancario. Cada cliente puede
        tener un máximo de 10 cuentas bancarias.
    """

    account_number = StringField(max_length=25, required=True)

    authorized = EmbeddedDocumentListField(BankAccountAuthorizedPerson, required=False)





# ======================================================================================================
# CLASS BANK CUSTOMER
# ======================================================================================================
class BankCustomer(Document):

    """
        Representa a un cliente del banco que puede tener una o más cuentas bancarias y 
        cada cuenta bancaria puede tener uno o más autorizados. 
    """

    # Nombre completo
    full_name = StringField(max_length=80, required=True)

    # Cedula de la persona
    personal_id = StringField(max_length=30, required=True)

    # Correo electronico
    email = StringField(max_length=60, required=True)

    # Direccion
    address = StringField(max_length=256, required=True)

    # Estado Civil
    marital_status = StringField(max_length=25, required=True)

    # Estado Civil
    salary = DecimalField(required=True)

    # Cuentas bancarias
    accounts = EmbeddedDocumentListField(BankAccount, required=False)

    # ------------------------------------------------------------------------------------------------
    # METODO LOAD
    # ------------------------------------------------------------------------------------------------
    def load(self, customer):
        self.full_name = customer.name
        self.personal_id = customer.personal_id
        self.email = customer.email
        self.address = customer.address
        self.marital_status = customer.marital_status
        self.salary = customer.salary

        try:
            # Persistimos el cliente en la base de datos
            self.save()
            return True
        except:
            return False

    # ------------------------------------------------------------------------------------------------
    # GET NUMBER OF ACCOUNTS
    # ------------------------------------------------------------------------------------------------
    def get_number_of_accounts(self):
        """
            Permite obtener la cantidad de cuentas bancarias que tiene una cuenta bancaria determinada
        :return: 
        """
        return len(self.accounts)

    # ------------------------------------------------------------------------------------------------
    # GET NUMBER OF ACCOUNTS
    # ------------------------------------------------------------------------------------------------
    def add_account(self, account):
        acc = BankAccount(account_number=account.account_number)
        self.accounts.append(acc)
        try:
            self.save()
            return True
        except:
            return False
