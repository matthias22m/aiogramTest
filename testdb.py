from ex.db_helper import Db_interaction
from ex.models import User

db = Db_interaction()

# db.insert_user(User(12,'girma bekele','girma@gmail.com'))

users = db.get_users()
print(users[0].name)