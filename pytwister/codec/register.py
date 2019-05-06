#!/usr/bin/env python
""" 
This file contains the information to register the pytwister encoding
""" 

import codecs, io, encodings
import sys
import traceback
from encodings import utf_8
import tokenize
from pytwister.codec.tokenizer import pytwister_tokenize

def pytwister_transform(stream):
    try:
        output = tokenize.untokenize(pytwister_tokenize(stream.readline))
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        raise

    return output.rstrip()

def pytwister_transform_string(input):
    stream = io.StringIO(bytes(input).decode('utf-8'))
    return pytwister_transform(stream)

def pytwister_decode(input, errors='strict'):
    return pytwister_transform_string(input), len(input)

class PytwisterIncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, input, final=False):
        self.buffer += input
        if final:
            buff = self.buffer
            self.buffer = b''
            return super(PytwisterIncrementalDecoder, self).decode(
                pytwister_transform_string(buff).encode('utf-8'), final=True)
        else:
            return ''

class PytwisterStreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        self.stream = io.StringIO(pytwister_transform(self.stream))

def search_function(encoding):
    if encoding != 'pytwister': return None
    # Assume utf8 encoding
    utf8=encodings.search_function('utf8')
    return codecs.CodecInfo(
        name = 'pytwister',
        encode = utf8.encode,
        decode = pytwister_decode,
        incrementalencoder = utf8.incrementalencoder,
        incrementaldecoder = PytwisterIncrementalDecoder,
        streamreader = PytwisterStreamReader,
        streamwriter = utf8.streamwriter)


# This import will do the actual registration with codecs
import pytwister.codec.fast_register
