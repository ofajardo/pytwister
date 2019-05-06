import codecs

def search_function(encoding):
    if encoding != 'pytwister':
        return None
    import pytwister.codec.register
    return pytwister.codec.register.search_function(encoding)

codecs.register(search_function)
