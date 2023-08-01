from faker import Faker
from peewee import *

db = PostgresqlDatabase(
    'customer',
    user='postgres',
    password='admin123',
    host='127.0.0.1')


class BaseModel(Model):
    class Meta:
        database = db


class Customer(BaseModel):
    name = TextField()
    bday = DateField()
    address = TextField()
    phone = IntegerField()
    marriage = BooleanField()

    class Meta:
        table_name = 'customer'
        primary_key = False


fake = Faker()
for i in range(0, 5000):
    q = Customer.create(name=fake.name(), bday=fake.date(), address=fake.address(), phone=fake.random_number(), marriage=fake.boolean()) 
    db.close()
