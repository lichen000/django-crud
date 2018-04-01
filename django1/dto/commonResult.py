import time

class CommonResult:
    code = 200
    message = "OK"
    data = None
    ts = int(round(time.time() * 1000))

    def __init__(self, code=200, message="OK", data=None, ts=int(round(time.time() * 1000))):
        self.code = code
        self.message = message
        self.data = data
        self.ts = ts

    def __setitem__(self, key, value):
        self.key = value
