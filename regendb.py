import json
from elo_funcs import regenerate_db, save_db
matches = json.load(open('matches.json'))
db = regenerate_db(matches, 'db.pickle')
save_db(db, matches)
