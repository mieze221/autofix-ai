# core.py
def check_internet():
    try:
        import urllib.request
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def hello():
    return "AutoFix is ready!"

