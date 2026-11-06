def publish(db, actor_id, note_id, after_check=lambda: None):
    note = db.execute("SELECT org_id FROM notes WHERE id=?", (note_id,)).fetchone()
    allowed = db.execute("SELECT 1 FROM members WHERE user_id=? AND org_id=? AND active=1", (actor_id, note[0])).fetchone()
    if not allowed:
        return "forbidden"
    after_check()
    db.execute("UPDATE notes SET status='published' WHERE id=?", (note_id,))
    db.commit()
    return "published"

