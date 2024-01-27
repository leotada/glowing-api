import unittest

from schema.bank_account import BankAccountSchema
from schema.base import ma

assert issubclass(BankAccountSchema, ma.Schema)