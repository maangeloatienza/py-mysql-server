from database.tables.users import Users

def index():
    users = Users()
    result = users.findAll()
    print(result)
    response = {
        'data' : result,
        'message' : "Successfully fetched users." if (len(result)) else "No users found"
    }
    return response