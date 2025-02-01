from database.Database import connect, cursor
from database.tables.init import Tables
from database.tables.users import Users

# roleTable = Tables('roles')
# roleTable.create("role VARCHAR(255), isActive TINYINT(1) DEFAULT 0")
user = Users()

# user.insert(values=["Mark Angelo", "Atienza", "maangeloatienza@gmail.com", "test"])

users = user.findOne(where=f"where id='9432ce47-a0be-46f5-9b42-99922c349009'")
print(users)