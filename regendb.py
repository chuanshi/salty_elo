import json
from elo_funcs import regenerate_db
matches = json.load(open('matches.json'))
regenerate_db(matches, 'db.pickle')