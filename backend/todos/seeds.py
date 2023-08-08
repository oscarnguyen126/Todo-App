from faker import Faker
from peewee import *



# find a way to interact with database via code
# maybe https://docs.peewee-orm.com/en/latest/

# 1. define mode
# 2. populate data using faker

db = PostgresqlDatabase(
    'todos',
    user='postgres',
    password='admin123',
    host='127.0.0.1')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = TextField()
    password = TextField()

    class Meta:
        table_name = 'users_user'


class Todos(BaseModel):
    description = TextField()
    is_done = BooleanField()
    complete_date = DateField()
    is_expired = BooleanField()
    user = ForeignKeyField(User, backref='todos')

    class Meta:
        table_name = 'todo_app_todo'
        primary_key = False


fake = Faker()
users = [user for user in User.select()]
for user in users:
    for i in range(0, 10000):
        q = Todos.create(description=fake.sentence(), is_done=fake.boolean(), complete_date=fake.date(), is_expired=fake.boolean(), user=user) 
        db.close()


# TODO: concurrency
# 1. Measure benchmark of current code
# 2. Spawn multiple processes to perform seeding (3-4), then measure benchmark again


# import process
import concurrent.futures


def seed_fn():
    # pass
#     fake = Faker()
# users = [user for user in User.select()]
# for user in users:
#     for i in range(0, 1000):
#         q = Todos.create(description=fake.sentence(), is_done=fake.boolean(), complete_date=fake.date(), is_expired=fake.boolean(), user=user) 
#         db.close()

thread_local = threading.local()
# a_process = process.Process() = worker
# b_process = process.Process()

about race conditions

[p.exec(seed_fn) for p in [a_process, b_process]]