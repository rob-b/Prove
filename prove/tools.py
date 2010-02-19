import re

def to_list(value):
    if value is None:
        value = []
    elif not isinstance(value, list):
        value = [value]
    return value

def inline(message):
    return re.sub('\s+', ' ', message)

def ok_(exp, message=None):
    assert exp, message

def eq_(a, b, message=None):
    if message is None:
        message = '%r != %r' % (a, b)
    assert a == b, message

def fail(message):
    raise AssertionError(message)

