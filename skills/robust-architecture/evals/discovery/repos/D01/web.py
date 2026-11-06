from library.commands import lend

def checkout(db,session,payload):
    return lend(db,session.library_id,int(payload['copy_id']),payload['borrower'])

