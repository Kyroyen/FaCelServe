
def userReponseEntity(user)-> dict:
    return {
        "id" : str(user["_id"]),
        "interest" : user["interest"]
    }