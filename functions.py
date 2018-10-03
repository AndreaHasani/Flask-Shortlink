from hashlib import md5
from string import ascii_lowercase


def md5Hash(s, digits):
    m = md5()
    m.update(s.encode())
    return m.hexdigest()[0:digits]


def shortlink(db, table, url):
    key = md5Hash(url, 8)
    db.session.add(table(str(key), url))
    db.session.commit()
    return key
