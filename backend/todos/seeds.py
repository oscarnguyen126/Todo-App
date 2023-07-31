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

class TodoAppTodo(BaseModel):
    description = TextField()
    is_done = BooleanField()
    complete_date = DateField()
    is_expired = BooleanField()

    class Meta:
        table_name = 'todo_app_todo'
        primary_key = False


fake = Faker()
for i in range(0, 100):
    q = TodoAppTodo.insert(description=fake.sentence(), is_done=fake.boolean(), complete_date=fake.date(), is_expired=fake.boolean()) 
    q.execute()
    db.close()
