import urllib2
import json

def read_state():
    """returns dict of state.json"""
    request = urllib2.Request('http://www.saltybet.com/state.json')
    request.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
    opener = urllib2.build_opener()
    try:
        data = opener.open(request).read()
    except:
	print "WARNING! Unable to obtain state.json.  Are you not logged in?"
        return {'status' : 'unreachable'}
    return json.loads(data)

def get_winner():
    state = read_state()
    if u'status' in state.keys():
        status = state[u'status']
        if status in ['1', '2']:
            return str(status)
    print "winner unknown. status is " + status
    return False

