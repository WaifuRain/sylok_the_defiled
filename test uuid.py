import uuid


def unique_id(user):
    discord_id = uuid.uuid4()
    return {user: discord_id}


id_db = {}
print(id_db)
id_db.update(unique_id('UncieDevin#7579'))
print(id_db)
