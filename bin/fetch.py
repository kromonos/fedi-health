import __main__
from urllib.request import urlopen
import json

class downloadData:
    def get(source):
        response = urlopen(source).read()
        return response.decode()