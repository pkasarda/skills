from notes import publish

def web_publish(db, session, note_id):
    return publish(db, session.user_id, note_id)

def cli_publish(db, service_actor, note_id):
    return publish(db, service_actor.user_id, note_id)

