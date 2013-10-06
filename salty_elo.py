from elo_funcs import *
from website_extract import *
import sys

def list_matches(player, db, matches):
        match_list = []
        for match in matches:
                if player in match:
                        other = list(set(match) - set([player]) - set(['1', '2']))[0]
                        if int(match[2]) - 1 == match.index(player):
                                wl = "W"
                        else:
                                wl = "L"
                        match_list.append([player, other, round(db[other].rating, 1), wl])
        match_list = sorted(match_list, key=lambda ml:ml[2])
        match_list.reverse()
        return match_list
                        

def predict(p1, p2, db, matches):
        predict_match(p1, p2, db) 
        print
        print p1 + "(" + str(round(db[p1].rating, 1)) + ")", "match history:"
        ml = list_matches(p1, db, matches)
        for m in ml:
                print m[3], m[2], m[1]
        print
        print p2 + "(" + str(round(db[p2].rating, 1)) + ")", "match history:"
        ml = list_matches(p2, db, matches)
        for m in ml:
                print m[3], m[2], m[1]

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
                    temp_query = raw_input('are you sure (y/n)? you should save first if you have not already!')
                    if temp_query == 'y':
                            sys.exit()
                    else:
                            print "input 'y' to quit"
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

