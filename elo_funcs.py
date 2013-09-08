import math
import pickle
import json

class Player:
	def __init__(self, name):
		self.name = name
		self.rating = 1500.0
		self.record = (0, 0)

def getExpectation(rating_1, rating_2):
	calc = (1.0 / (1.0 + pow(10, ((rating_2 - rating_1) / 400))));
	return calc;
def modifyRating(rating, expected, actual, kfactor):
	calc = (rating + kfactor * (actual - expected));
	return calc;
def add_match(p1, p2, winner, db, matches, real=True):
	if p1 not in db.keys():
		db[p1] = Player(p1)
	if p2 not in db.keys():
		db[p2] = Player(p2)
	if winner not in ['1', '2', 1, 2]:
		print 'winner must be 1 or 2'
		return False

	p1_expec = getExpectation(db[p1].rating, db[p2].rating)
	p2_expec = 1 - p1_expec

	kf1, kf2 = 30, 30
	if sum(db[p1].record) > 30:
		kf1 = 15
	if sum(db[p2].record) > 30:
		kf2 = 15

	db[p1].rating = modifyRating(db[p1].rating, p1_expec, -int(winner) + 2, kf1)  # hack to be 1 if p1 wins, 0 if p2 wins
	db[p2].rating = modifyRating(db[p2].rating, p2_expec, int(winner) - 1, kf2)   # hack to be 1 if p2 wins, 0 if p1 wins
	if real:
		matches.append([p1, p2, str(winner)])
	return True

def predict_match(p1, p2, db):
	if p1 in db.keys():
		print p1, 'rating is', db[p1].rating
	if p2 in db.keys():
		print p2, 'rating is', db[p2].rating
	if p1 in db.keys() and p2 in db.keys():
		print getExpectation(db[p1].rating, db[p2].rating) * 100., "% ", p1, "wins over", p2
	if p1 not in db.keys() and p2 not in db.keys():
		print 'no info'

def save_db(db, matches):
	pickle.dump(db, open('db.pickle', 'w'))
	json.dump(matches, open('matches.json', 'w'))

def regenerate_db(matches, outname):
	"""
	rebuilds a db.pickle out of a matches.json
	"""
	new_db = {}
	for match in matches:
		add_match(match[0], match[1], match[2], new_db, matches, real=False)
	pickle.dump(new_db, open(outname, 'w'))

