from elo_funcs import *
from website_extract import *
import sys

def predict(p1, p2, db, matches):
        predict_match(p1, p2, db) 

	for match in matches:
		if p1 in match:
                        other = list(set(match) - set([p1]) - set(['1', '2']))[0]
			if int(match[2]) - 1 == match.index(p1):
				print "{0} beat {1}({2})".format(p1, other, db[other].rating)
			else:
				print "{0}({2}) beat {1}".format(other, p1, db[other].rating)

	for match in matches:
		if p2 in match:
                        other = list(set(match) - set([p2]) - set(['1', '2']))[0]
			if int(match[2]) - 1 == match.index(p2):
                                print "{0} beat {1}({2})".format(p2, other, db[other].rating)
			else:
				print "{0}({2}) beat {1}".format(other, p2, db[other].rating)


if __name__ == "__main__":
    reset = False
    if len(sys.argv) > 1 and sys.argv[1] == "--resetdb":
            reset = True

    if not reset:
            db = pickle.load(open('db.pickle', 'r'))
            matches = json.load(open('matches.json', 'r'))
    elif reset:
            import shutil
            try:
                    shutil.copy('db.pickle', 'db.pickle.old')
                    shutil.copy('matches.json', 'matches.json.old')
            except:
                    pass
            db = {}
            matches = []

    while True:
            query = raw_input('command? ("(a)dd", "(p)redict", "(q)uit", "(s)ave"), "(l)ist"')
            if query == 'q' or query == 'quit':
                    save_db(db, matches)
                    sys.exit()
            elif query == 'p' or query == 'predict':
                    p1 = raw_input('player 1?').upper()
                    p2 = raw_input('player 2?').upper()
                    predict(p1, p2, db, matches)
            elif query == 'a' or query == 'add':
                    p1 = raw_input('player 1?').upper()
                    p2 = raw_input('player 2?').upper()
                    winner = raw_input('winner? (1 or 2 or query)')
                    if winner == "query":
                            winner = get_winner()
                    result = add_match(p1, p2, winner, db, matches)
                    if result:
                            print 'new', p1, 'rating is', db[p1].rating
                            print 'new', p2, 'rating is', db[p2].rating
            elif query == 's' or query == 'save':
                    save_db(db, matches)
                    print "saved!"
            elif query == 'l' or query == 'list':
                    chars = db.keys()
                    elos = []
                    for char in chars:
                            elos.append(db[char].rating)
                    yx = zip(elos, chars)
                    yx.sort()
                    yx.reverse()
                    for i in range(len(yx)):
                            print yx[i][1].rjust(30), str(yx[i][0]).ljust(32)
                    print len(chars), "number of characters recorded"
                    print len(matches), "number of fights recorded"
            else:
                    print "Command not recognized"

